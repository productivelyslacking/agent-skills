# godot-dotnet: notes

Facts seen on one project, kept for whoever hits the same thing. They haven't recurred enough to be rules, so check them against your versions. Moved from `docs/CANDIDATES.md` on 2026-11-07 (D21).

- **2026-10-04, action-rpg - Don't name engine-free sim types after engine classes.** A sim
  `Container` compiled alone, then clashed with `Godot.Container` in every game script using both
  namespaces (CS0104). Pick names the engine doesn't use (`LootContainer`). Target: godot-dotnet.
- **2026-10-04, action-rpg - Reset a change-detection key to a value no real state produces.** A view
  cache keyed on a joined id list was reset to `""` on area change, which an empty area also yields,
  so the old area's NPCs stayed drawn. Use `null` (or a generation counter). Reproduce by moving
  between states, not by starting in one. Target: godot-dotnet or new: game-presentation.
- **2026-10-04, action-rpg - Godot retargeting can be set up headless, in the `.import` file.** Import
  once, then set `_subresources={"nodes": {"PATH:<skeleton path>": {"retarget/bone_map":
  Resource("res://<map>.tres")}}}` and import again; a BoneMap `.tres` is `bone_map/<ProfileBone> =
  &"<model bone>"` over a `SkeletonProfileHumanoid` (generate one with a script to see the format).
  Both skeletons become `%GeneralSkeleton` with profile bone names, so one AnimationLibrary plays on
  every body. Godot drops `_Loop` from animation names on import. Target: godot-dotnet.
- **2026-10-04, action-rpg - Godot's `ResourceLoader.Exists` answers from the `.import` file.** True with
  the source model and its imported copy both gone; a fallback keyed on it never fired. Check that it
  loads. When testing "the file is missing", also move `.godot/imported/<file>-<hash>.*`: the cache
  keeps drawing it and the test passes for the wrong reason. Target: godot-dotnet.
- **2026-10-04, action-rpg - A retargeted import can leave a skin's bind names unrenamed.** The skeleton
  became `GeneralSkeleton` with profile bone names, but the mesh's Skin still bound `thigh_l`; moved
  onto another skeleton, Godot logged an error per bone and bound by index (right only by luck of
  order). Rename binds through the bone map when re-parenting skinned meshes, and read the log of a
  headless run even when the render looks fine. Target: godot-dotnet.
- **2026-10-04, action-rpg - Godot: change import settings by regenerating the whole import cache.** Deleting some `.import` files to pick up a new default gave the textures new UIDs the cached model
  scenes didn't know; the exported build logged "invalid UID" for each. Delete `.godot/imported`, the
  uid cache and any extracted files, then import once (the fresh-clone state). And cap texture size
  with `[importer_defaults] texture={"process/size_limit": N}` for handheld targets: a free asset
  pack's 4K textures took a build from 15 MB to 719 MB. Target: godot-dotnet.
- **2026-10-04, action-rpg - Godot: don't quit in the frame you take a scripted screenshot.** A shot that
  quit the same frame a label first drew new glyphs never exited (bisected to the text; already-cached
  letters were fine). Save, then quit a few frames later. And `timeout` around a wrapper script leaves
  its gamescope/Godot children running: hung runs piled up and exhausted the GPU (`vkCreateDevice -3`).
  Kill the children, or put the timeout on the engine itself. Target: godot-dotnet.
- **2026-10-04, action-rpg - Godot: headless imports leave 3D textures uncompressed.** A texture's
  default is lossless with "detect 3D → VRAM compressed", and only the editor does the detecting; a
  project imported headless (CI, export, fresh clone) sends every model texture to the GPU at four bytes
  a pixel. Set `compress/mode=2` in `[importer_defaults] texture` and keep UI images lossless in their
  own committed `.import` files. Measured: 280 → 140 MB of texture memory in one level, and a smaller
  package. Target: godot-dotnet.
- **2026-10-05, action-rpg - Godot: measure the game's audio with the movie writer.** `--write-movie
  out.avi` (under headless gamescope; the dummy renderer crashes it) records the game's own mix with the
  video; `ffmpeg -af volumedetect` then compares two builds' loudness. To A/B an asset swap, moving the
  source file aside isn't enough: the imported copy in `.godot/imported` still loads. Move that too, or
  the "before" run is the "after" run. Target: godot-dotnet.
- **2026-10-05, action-rpg - Under headless gamescope, Proton's orphaned winedevice.exe keeps gamescope alive after the game quits.** gamescope's reaper waits for every descendant; `winedevice.exe` survives the game in its own session, ignores TERM, and holds the run open forever, so `timeout` without `-k` hangs. Stop what's left in the run's own Wine prefix (match WINEPREFIX in `/proc/PID/environ`), TERM then KILL, and wrap gamescope in `timeout -k`. Never kill by process name on a handheld: the headless gamescope has the same name as Gaming Mode's compositor. Target: godot-dotnet.
- **2026-10-05, action-rpg - Test a Godot C# class's pure half by splitting it with `partial`.** Settings' file shape and parsing went into a Godot-free `Settings.cs`, linked into the engine-free test project (`<Compile Include="../../game/scripts/Settings.cs" Link=... />`); its load, save and audio stay in `SettingsIo.cs`, which the tests never see. Target: godot-dotnet.
- **2026-10-05, action-rpg - Graphics steps measured one at a time didn't add up.** In a rift each High step alone cost at most +0.03 ms of GPU, but all together cost +0.37 ms (outdoors they roughly added up). Measure the whole preset as well as each step, and report both. Target: godot-dotnet.
- **2026-10-05, action-rpg - Square brackets in Godot's RichTextLabel are BBCode tags.** "[Hask's Notice 1:39]" printed raw and swallowed the following `[/color]` and `[b]`, which then printed as text. Write `[lb]`/`[rb]` for a literal bracket in rich text; plain Labels are unaffected. A still caught it, not the build. Target: godot-dotnet.
- **2026-10-05, action-rpg - Grepping a `dotnet test` run for test lines hides a compile error.** A probe that didn't compile printed nothing through `grep -E 'Passed|Failed'`, and the next `--no-build` run quietly ran the previous assembly's tests. Build first and grep for ` error`, or never pass `--no-build` after an unchecked build. Target: godot-dotnet.
- **2026-10-06, action-rpg - `ReloadCurrentScene()` called mid-`_Process` leaves the rest of that frame running outside the tree.** Quitting to the title from a menu inside `Main._Process` gave a NullReferenceException (`GetViewport()` null) and two "not inside tree" engine errors on every return. No stale reference was involved. Return from `_Process` right after asking for the reload (or defer it). The same restart left a resize-signal lambda connected to the freed node, so each return added one and every later resize threw; connect named methods and disconnect them in `_ExitTree`. Found by a pad-driven quit-and-continue run whose log is grepped for errors, which failed on main. Target: godot-dotnet.
- **2026-10-06, action-rpg - Before stills rendered from the worktree being edited pick up the edits.** A render script that mirrors the live checkout per still, with shaders read from source at run time, put a shader edit made mid-batch into later "before" stills, silently. Render "before" from a clean detached copy, or freeze the tree until the batch ends. Target: agent-team (evidence) or godot-dotnet.
- **2026-10-06, action-rpg - A Godot node made only to read a property leaks, and a hand-copied engine shader drifts.** `Sun().Basis.Z` built a new DirectionalLight3D every time it was read and never freed it: 70 leaked objects in one autoplay run, invisible except in a verbose run's leak report. Compute the value, or free the node, and keep a leak check that fails on the old code. The same branch copied Godot's procedural sky shader from an older version: 4.7.2 converts colours with `source_color` and the curves as 0.6/curve and 1.6/curve^1.4, so the copy lit the world 11% brighter while the branch said "lighting unchanged". Port from the exact engine version's source, and prove "unchanged" with a same-frame pixel comparison against the engine's own material. Target: godot-dotnet.

## The toolchain's lies

- Learned on an action RPG: Godot 4.7.2 .NET, net10.0, built headless on a NAS.
- **CS0108:** the `const float Size` on a `Control` hid `Control.Size`; every unqualified `Size` in the class meant the
  constant.
- **Proton:** `umu-run Game.console.exe --headless ...` exited 0 printing only Proton's lines; the result was only in
  Godot's log inside the prefix.
- **Seeds:** a seed from `GetHashCode()` ("the same scatter for this area every time") moved every launch.

## What must be committed, and what the export drops

- **Repeated kit textures:** 24 identical 1024² copies cost 60 MB of texture memory in one level while adding under 1 MB
  on disk.

## Seeing it without a display

- **Headless audio leak:** `AudioStreamWAV`/playback instances were reported leaked, the count following how many sounds
  played; releasing every cache on exit changed nothing.
- **Software rendering:** mirrored worlds, overlapping HUD text and lists running off-screen were only ever caught this way.

## Seeing it move, and driving it, without a person

- **Contact sheet:** ten seconds of play reviewed at a glance found units standing inside each other in every melee
  fight; every test passed, and stills read it as clutter. A frame deep into an autoplay run under headless gamescope
  takes minutes.
- **Pad events:** found raw glyph markup in a plain `Label` and a held modifier losing to a context binding.
