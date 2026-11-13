---
name: godot-dotnet
description: Building, exporting and checking Godot 4 C# projects, especially headless or in CI, where the toolchain fails silently. Use when touching a Godot C# build, export, CI or tools, or when a Godot run's result looks wrong.
---

# Godot with C#

Assumes **ground-truth**. Godot's .NET toolchain fails quietly more often than loudly: every rule here is a case where
the tool reported success on a broken result. Re-check version-specific details against the version in use. The
versions these were learned on, the measurements, and traps seen once are in `NOTES.md` beside this file; read it when
a Godot build, import, export or headless run misbehaves.

## The toolchain's lies

- **Check scripts with `dotnet build <game>.csproj`, not `--build-solutions`:** the latter prints `[ DONE ]` on code
  that doesn't compile. Prove it once by planting a type error.
- **Build before any script runs Godot** (screenshots, autoplay, exports), and stop on a compile error: Godot silently
  runs the last-built assembly.
- **Check the export's contents, not its exit code:** a failed .NET publish still exits 0 and writes the `.exe` and
  `.pck` without the `data_<project>_<platform>/` folder, so the build launches and does nothing.
- **Make "ExportRelease" optimize plain class libraries in `Directory.Build.props`:** Microsoft's SDK only optimizes a
  configuration named exactly `Release`, so they ship as debug builds. Verify by each DLL's `[Debuggable]` attribute.
- **Give headless runs their own deadline with a non-zero exit,** and pass only when the outcome line prints:
  `--quit-after N` exits 0, so a stuck run looks like a pass.
- **`--fixed-fps` is virtual time:** fast for end-to-end checks, but real networking or a separate process needs
  wall-clock time (`--max-fps`).
- **Treat CS0108 in engine scripts as an error:** a member named like a Godot property (`const float Size` on a
  `Control`) hides it, and only a warning says so.
- **Set `DOTNET_ROOT` for a user-level SDK where the launcher reads it** (`~/.config/environment.d/` or the launcher's
  `Exec=`), and test with `env -i`: Godot aborts with "Failed to load hostfxr", and a working shell proves nothing
  because launchers don't read `~/.bashrc`.
- **Under Proton, judge a Windows build by Godot's log inside the prefix**
  (`drive_c/users/steamuser/AppData/Roaming/<app>/logs/godot.log`), from a fresh prefix: console output doesn't reach
  you, and an old log can answer for a run.
- **Seed with a stable hash such as FNV-1a, never `string.GetHashCode()`:** .NET randomises it per process.

## What must be committed, and what the export drops

- **Commit each script's `.uid` and each asset's `.import`; ignore `.godot/`.** A new script's `.uid` appears only on
  import, so run `godot --headless --path <game> --import` before committing it, or the next export stamps the build
  "uncommitted changes".
- **Embed plain data files or add an include filter:** the export packs resources only, so JSON read through `res://`
  works in the editor and is missing from the export. Use `<EmbeddedResource>` with a `LogicalName`, then check the
  exported build has it.
- **Match the Godot.NET.Sdk version to the editor build exactly.**
- **Import extracts a model's embedded textures beside it** (`<name>_<texture>.png` and its `.import`): ignore them with
  the model when models aren't committed, and have art checks count only the asset types placed there.
- **Unpack a kit of `.glb` pieces that embed the same texture to `.gltf` with one shared image:** each piece becomes its
  own GPU copy, and the package size hides it. `md5sum` a new kit's extracted textures, and measure with
  `RenderingServer.GetRenderingInfo(RenderingInfo.TextureMemUsed)`.

## Coordinates

- **Godot's forward is −Z.** Mapping a 2D sim's north (+y) to +Z mirrors the world, and every test passes because the
  sim is right and nothing tests the drawing. Check one known direction end to end ("east of you appears on your
  right"), in one conversion function used everywhere.

## Seeing it without a display

- **Rerun with a real audio driver and the volume above zero before chasing an exit leak under `--headless`:** the dummy
  driver never mixes, so it reports every played sound as leaked, and a muted master does the same.
- **Check layout with software rendering in a container:** Xvfb plus Mesa,
  `--rendering-method gl_compatibility --rendering-driver opengl3`, and a dev argument that saves frame N as a PNG. It
  catches mirrored worlds and overflowing UI; it says nothing about the real renderer, performance or feel.
- **Start `Xvfb :99` yourself as a non-root container user,** wait for `/tmp/.X11-unix/X99`, then run with
  `DISPLAY=:99`: `xvfb-run` waits for a signal that never comes.
- **Run SDK containers with `--user $(id -u):$(id -g)`,** or `bin/` and `obj/` end up root-owned on the host.
- **Give the game dev arguments that open a screen** (`--menu=inventory`) and load a save from a given home folder, with
  state built by the game's own save code: most screens only look wrong with real data in them.

## Seeing it move, and driving it, without a person

- **Use headless gamescope for the real renderer with no display:**
  `gamescope --backend headless -W 1280 -H 800 -- godot ... --screenshot-frame=N` renders Forward+ on the real GPU, at
  real time.
- **Review motion as a contact sheet:** Movie Maker (`--write-movie clip.avi --quit-after N`) records every frame and the
  audio; tile two frames a second with ffmpeg (`-vf "fps=2,scale=640:-1,tile=4x5"`). It catches motion bugs that tests
  and stills miss; a deterministic autoplay lets you find the frame in the sim first. ffmpeg's `volumedetect` and a
  `showspectrumpic` spectrogram show whether each sound fires, not whether it sounds good.
- **Drive the UI with injected pad events:** a dev argument that plays timed `Input.ParseInputEvent` of real
  `InputEventJoypadButton`/`Motion` tests the bindings too, and reaches UI bugs no unit test can. Use a throwaway home:
  it saves for real.

## Engine boundary

- **Keep game rules out of engine scripts:** a plain C# library holds them, tested headless with `dotnet test`, so the
  engine-side checks shrink to "does it build, render, and finish autoplay". See **game-simulation-testing**.
