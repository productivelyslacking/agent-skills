# game-assets: notes

Facts seen on one project, kept for whoever hits the same thing. They haven't recurred enough to be rules, so check them against your versions. Moved from `docs/CANDIDATES.md` on 2026-11-07 (D21).

- **2026-10-04, action-rpg - Blender's glTF importer adds a hidden 2 m bone-shape sphere.** It sits in
  a `glTF_not_exported` collection at the origin; measuring "all meshes" counted it and stood bodies a
  metre up, 2.81 m tall. Skip that collection (and hidden props) when measuring imported models.
  Target: game-assets or new: blender-scripting.
- **2026-10-05, asset-pipeline - Mirror-tiling makes directional textures wrong, and a symmetric seam check
  passes it.** Quarter-turn/mirror tiling made roof tiles flip at every edge and drew a frame round each
  repeat, yet the seam score was 0.0 because the border was exactly symmetric. For directional patterns,
  tile by translation (crop to where the pattern repeats in phase, crossfade) and check the seams against
  the texture's own line spacing. Also: asking an image model to inpaint a seam cross invents objects
  (pipes, brackets) along it. Target: game-assets.
- **2026-10-05, action-rpg - Thin upright props read black under a top-down camera when every light
  comes from above or behind.** Weapons read near-black in a dark dungeon and in daylight while barrels
  read fine: a blade's camera-facing sides get no direct light and it has no top to catch it, and metal
  (generator metallic maps, 0.8–0.93 even on wood) reflects a black room. Toggling ambient, shadows,
  SSAO, fog and reflections one at a time changed nothing; a camera-side fill culled to a held-prop
  layer, plus a metallic cap, fixed it without touching the scene's light. Render the prop unshaded
  beside its lit self before blaming albedo. Target: game-assets ("Engine specifics") or new:
  game-presentation.
- **2026-10-05, action-rpg - A seam check against one pooled threshold fails natural textures
  that have no seam.** Grass, earth and gravel have a bright blade or stone somewhere on almost every
  line, so a line's worst 32 px stretch reached 1.1-1.5 times the texture's pooled 99th percentile and the
  check failed even the raw image's middle, where there is no seam. Rank each seam against the
  distribution of the texture's own interior lines (its mean and its worst window under their 99th
  percentiles), and keep the proof that it can fail: the raw image's edges must fail it (they did,
  1.04-1.54; the tiles passed, 0.81-0.97). Mortared masonry does the same (dark joints on every line:
  the window test failed every stone seed's seam-free middle, up to 1.85). A normal map derived from
  the texture with wrapped differences is periodic by construction, and the same statistic fails its
  middle too: don't gate normal maps on it. Target: game-assets.
- **2026-10-05, action-rpg - A texture prompt drew an object until the framing came first.** Description + the house style + a "fills the frame" staging passed CLIP's 77 tokens, so the staging
  was cut, and the style's "game asset" made all 30 seeds a heap or patch on a plain background. Leading
  with "seamless top-down texture of X covering the entire image", a short material-only style and a
  short positive staging, every seed filled the frame. Target: game-assets (with the generator rules).
- **2026-10-05, action-rpg - Generated ground comes out in the effects' colours; measure hue before
  judging.** Every "bare earth" seed was orange, the colour of telegraphs and burning ground; toned to
  saturation 0.4 it still read orange under a warm sun and filmic tone mapping. Measure the texture's
  mean hue and saturation (it ended at 0.07) and look in the game's light, not the swatch. Target: game-assets.
- **2026-10-05, asset-pipeline - Image-to-3D needs the sides in the concept; measure "solid" as the largest
  connected piece.** A gateway concept drawn flat front-on came out of TRELLIS.2 as loose stone faces
  or a deep hollow box on four sampling seeds (largest piece after welding by position: 15-48% of
  the faces); the same object drawn from a front corner, "a few large blocks, the sides visible",
  gave one solid piece (95.8%). Reroll the concept, not the 3D seed, when the depth is wrong. Target: game-assets.
- **2026-10-05, asset-pipeline - Image-to-3D paints non-metal materials metallic.** A wooden bow came out
  0.93 metallic, a wooden staff 0.45, a leather shield 0.44; metallic surfaces reflect a dark scene
  and render near black there. Measure every generated asset's mean metallic (texture blue channel
  times factor) and cap it for single-material non-metal objects; mixed objects need a mask, a
  global cap kills the metal parts. Target: game-assets.
- **2026-10-05, asset-pipeline - Thin modular pieces don't survive image-to-3D at low budgets.** Wall panels
  at 250-400 triangles came out as a closed box (squashed into a slab, torn through), a sheet with
  holes, or near-black stone with gaps, while props at the same budgets were fine. For pieces that
  must meet their neighbours, use a simple mesh with a tiling texture. Confirmed by building them in code (roofs,
  then walls): each to the placeholder's measured box, the walls passed at 26-900 triangles with
  real window and door openings; check the openings by rasterising the front view against the
  placeholder's, so a door leaf placed by the engine still fits. Target: game-assets.
- **2026-10-05, action-rpg - Don't fit an asset smaller than the box the engine stretches it to.** A
  rock scaled uniformly to keep its proportions filled 71% of a footprint the game scales every rock
  to anyway, leaving invisible collision round it. Check how the code places an id before choosing
  how the file fits its box. Target: game-assets.
- **2026-10-05, asset-pipeline - A deformation test that measures stretch passes a mesh that doesn't move.** Bone
  heat failed and left every vertex unweighted; the edge-stretch score was a perfect 1.0. Pair it with a
  floor on how far each clip moves the mesh against the reference's, and a rigid control (all weights
  on one bone also stretches nothing: only a weight-reach test catches it). Target: game-assets.
- **2026-10-05, asset-pipeline - Blender's glTF import splits vertices along UV seams; bone heat on that fails for
  every vertex with only a warning.** A cleaned 5,000-triangle model came in as 887 pieces. Weld a
  copy, weight it, give each original vertex the weights of the welded vertex at its place. Target: game-assets.
- **2026-10-05, asset-pipeline - Sampling several actions in one Blender session: a channel the next action doesn't
  key keeps the last one's value.** A wolf's Idle sampled after its Death showed 79 stretched edges
  at frame 0, none from a fresh load. Reset every pose bone to rest before switching actions. Target: game-assets.
- **2026-10-05, asset-pipeline - FLUX schnell image to image has no useful strength at its 4 steps.** From a pose
  guide, 0.5-0.7 left the guide nearly untouched and 0.85 ignored it (two different guides, identical
  images). At 8 steps 0.85 kept the stance, but the guide's colour survived; a guide rendered in the
  target's colouring gave the creature in the guide's pose. Target: game-assets.
- **2026-10-05, asset-pipeline - Blender's glTF exporter writes a skinned mesh in world units under its armature's node scale.** A CC0 wolf whose armature node carries x100 came back from a plain import and export 100 times larger by its box (555 against 5.55); skinning still placed it right, but the game sized models from the mesh box times the node scale and drew it too small to see. Every check passed until a size check against the source file was added. Apply the armature object's transform to its bones before exporting (scale location keys to match), and gate the exported box against the source's. Target: game-assets.
- **2026-10-05, asset-pipeline - Fine colour detail in a concept rarely survives image to 3D; measure it before deriving a mask from it.** The brief was "make the cracks glow, from the warm texels". The Ember Hound's concept had thin orange cracks. TRELLIS's texture kept 0.24% of texels warm, and those were specks (the eyes), not lines. After the cleanup's re-bake 0.008% were left. A mask from the base colour would have lit nothing, and the check would have caught that only through its minimum cover. Count the feature's texels in each stage's texture first. If it's gone, author it on the surface (here: 3D Voronoi edges on the rest pose, baked into the UVs), paint it into the base colour, and derive the glow from that. Also: judge emissive coverage at the game camera, not in a close preview. 17% lit read as patches in game, and 15% with thinner lines read as cracks. Target: game-assets.
- **2026-10-06, asset-pipeline - An outline score passes a shredded mesh; pair it with genus and see-through.** Generated props were scored by outline IoU against their concept (holes filled, so the cradle's arch doesn't count). A keg rebuilt into a lattice of slits scored 0.943, beside 0.954 for a whole one. Two more measures caught every shredded case by eye: the share of the outline open to the background from 8 views (8.5% against 0.0) and the welded mesh's genus (29-44 against 0-10), which also catches holes that show the dark inside rather than the background. A back-face share, tried first, didn't separate them: the generator's face winding is inconsistent. Target: game-assets.
- **2026-10-06, asset-pipeline - A voxel remesh's first voxel decides whether an open generated shell comes out whole, and not monotonically.** The same TRELLIS crate stack rebuilt at 1% of its size had genus 39 (slits through every face), at 1.5-3% genus 0; another seed was whole at 1% and 3% but shredded at 1.5%. Rebuild at several voxels and score each; don't fix one. Target: game-assets.
- **2026-10-06, asset-pipeline - A GPU image job can write black images and exit 0.** FLUX schnell on the RX 9070 (ROCm) wrote 22 of 24 images as all-black (NaN, a numpy "invalid value encountered in cast" warning only); a re-run an hour later was fine; the cause wasn't found (the card was busy with another job at the time). Check every image for NaN or near-black before it's used. Target: game-assets, or ground-truth (rule 6).
- **2026-10-06, asset-pipeline - "Show the same object from behind" in an image-edit model gives a mirror image, not a rotation.** Qwen-Image-Edit-2511 drew the keg's back as the front flipped, a tap on each head; FLUX.2 klein 4B returned nearly the input. Fed to TRELLIS.2 as extra views, the mirrored one made the model worse (outline IoU 0.975 to 0.956, taps doubled into spikes), while true renders of a known prop as extra views helped (a cart's back view IoU 0.77 to 0.90). Test multi-view conditioning on rendered ground truth before trusting generated views. Target: game-assets.
- **2026-10-06, action-rpg - Naming a light source in an image prompt paints it.** "A pale veiled sun glow" gave a sun disc in six of six FLUX seeds, at the wrong height for the game's light; "soft diffuse even light across it" gave none in five of six. Describe how light falls, not its source, when the engine supplies the source. Target: game-assets.
- **2026-10-06, action-rpg - A painted sky can make HUD text over it unreadable.** The first sky band raised the luminance behind the close camera's top-left HUD text from 0.375 to 0.898 (near-white). Measure the HUD's background strip in before/after stills when a backdrop changes; darkening a golden painting too far turns it muddy, so balance against outlined text. Target: game-assets (readability).
- **2026-10-11, 3d-game - Judge a colour under the scene's own light, several candidates in one still.** A tan vest picked from the palette read as bare skin from the game's camera under a violet key light, and an olive one looked brown in a still whose palette import was stale. Six vest colours built as variants and stood side by side in one in-engine lineup settled it in one render (charcoal vanished on the floor, khaki and brown sat on the skin, olive held). Pick colours from a side-by-side still at the game's camera and light, not from swatches. Target: game-assets.
- **2026-10-11, 3d-game - Gear meant for bodies of more than one build carries the build's shape key itself.** A vest fitted to the standard body let the broader "Brute" body's shirt show through. Each piece got the same shape key, built from the body's nearest vertex's offset, and the game turns it on with the body's: one piece fits every build. Target: game-assets (modular characters).

## Game assets (moved from SKILL.md, 2026-11-13)

- The skill was learned on an action RPG whose placeholders were Kenney input prompts and game-icons.net icons, set
  up to be replaced.

## Engine specifics (moved from SKILL.md, 2026-11-13)

- **Debug colour:** placeholder armour on chunky stylised bodies was created and placed right but swallowed by the
  limbs; painted magenta, one render showed a sliver. Sized to show, the pieces would have been balloons: the fix
  was to wait for art made in pieces.
