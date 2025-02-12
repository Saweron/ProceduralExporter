# Reasons to develop my own model exporting library:
## Texture Baking:
### Manual texture baking can be extremely tedious:

- Manually clicking the "render" button up to 5x per model segment to bake all maps is slow, error prone, and above all else, encourages putting off texture baking until the last minute due to how annoying the whole process is.

- Failure to check that the proper image texture is selected inside of each material's node graph before clicking "render" can lead to previously baked texture maps being overwritten. Often it isn't even possible to undo such mistakes. This means that on top of having to re-render the current set of textures, you also have to go back and re-render the texture maps affected by your mistake. Manually triple-checking that the proper images are selected is slow, stressful, and exhausting.

- After those two steps, you still have to re-combine all the textures into a single atlas if you wanna reduce drawcalls. This means going through the nightmarish process of baking each map of each material into a single atlas, one after another. As explained in the two points above, doing so is extremely unpleasant and slow.

### While there are alternatives. Every texture baking tool I've found always has some dealbreaker that makes using it just as, if not more inconvenient than manual baking:

- Substance Painter, the most recommended alternative is quite expensive. This wouldn't be  much of an issue if I could pay once to use it. If that were the case, I'd have no problem giving it a try. Unfortunately, it's expensive AND subscription-based. If you stop paying, you lose access to an offline program installed on YOUR hard drive, on YOUR computer that YOU own. It makes me angry that a megacorporation thinks it has the AUDACITY to tell me what I own on MY computer, as if they can reach into it and yank things out. I prefer FOSS software for this exact reason. I like autonomy. I like owning the stuff on my computer. And anyway, I find Blender's node-based texturing approach to be more fun and intuitive than Substance Painter's layer-based approach. as a programmer, I find that the node-based workflow map better to my way of structuring things.

- All the Blender plugins for texture baking are either too limited, too expensive, too inconvenient, or some mixture of those three. Some Blender plugins force you to adopt a layer-based textureing approach, which I've previously expressed my distain for. Some of the plugins force you to arrange your nodes a particular way to be able to bake all the texture maps. And of course, paid plugins go against the "F" in "FOSS", so I try to avoid them whenever possible.

### Texturing would be way more fun if I didn't have to constantly think about how I'm going to bake my creation for exporting

- Because of how tedious baking is, I often simplify my textures to make the eventual process more tolerable. A side effect of this is that my texturing often looks "boring" because of its simplicity. I wanna be able to make more complex textures without needing to worry about the logistics of baking it all in the end.

- If I automate baking with my own custom solution, I could go back to make some tweaks to my model textures, then re-bake in a couple minutes. There's been so many instances where I make some mistake while texturing and it's more convenient to hastily paint over the baked texture than to re-bake everything.

## Compilation improves performance

### Draw call minimization

- The more meshes a model consists of, the more drawcalls you have to perform. Obviously, that's bad. Joining those meshes together before exporting a model is good practice, but it's often not worth the hassle when doing it manually. Once you join the meshes together, some information is lost. For example, one mesh's pivot point is discarded when joining the two together. You could always re-join the meshes at the very last moment before exporting, but that's also tedious and prone to mistakes. In my model exporting library, I want to include some functions for quickly combining meshes together automatically as part of the export preparation process.

### Automatic decluttering

- A mesh often has vertex groups used to control which vertices a modifier can operate on. I'm not sure if Blender's .fbx and .glb model exporters automatically remove these groups, but I do know that exporting a .blend file containing the final model and textures sure doesn't. Even if it doesn't matter much, It would be nice to automatically strip the export-prepared model of unnecessary clutter.

- A Blender scene often includes a bunch of empties and proxy objects for driving effects and modifiers. Manually cherrypicking the relevant meshes out from between these development objects every time I want to export is quite annoying

## Character-specific stuff

### Clothes

- Adding clothes to a character usually means fitting the clothing item to the character's body, transferring the weights to the clothing item, then sometimes giving the clothing item its own shape keys to match the underlying body's shapekeys. If a character has some shape keys for adjusting expressions, proportions, volume preservation, etc, the same deformations need to be applied to the clothing mesh. Copying the shapekeys manually is quite tedious. Additionally, to avoid clipping issues where parts of the character's body pokes through the clothing item during deformations, it's often a good idea to "squish" the character's underlying body down. Automating these sort of things would be nice.

- If you want to hide certain clothing items, you either split them into their own meshes, or you create a shapekey where the clothing item is hidden. Often this just means shrinking the clothing item down and hiding it inside the character's body mesh. A more optimal solution would be to make every triangle in the clothing item point somewhere where it'll always be backface culled. The way I'd do this is by making each triangle occupy the same 3 points inside of the character's body such that every triangle points downward. Doing this manually would be ridiculous, but it should be relatively straightforward to iterate through every triangle in a clothing item mesh.

### Expressions and deformations

- It's generally not a good idea to manually sculpt a character's expressions directly on their face mesh, instead I reshape a "proxy" mesh and apply its deformations to the face. This means I can reuse the expression deformations on other characters. The downside of doing it this way is that I have to apply the deformation on the proxy mesh, bake the deformation on the character mesh to a shape key, then repeat for every expression. It's three button presses, yet Blender doesn't give me a way to do it automatically without the use of some niche plugin.

- Going from shape A to shape B on a character's mesh often necessitates the use of additional in-between shapekeys. This means making an animation track for interpolating between the two. Again, making these simple tracks manually is quite tedious, so automating them would be nice.

## Full Control

- Other plugins that simplify the exporting process often only address one aspect. This means that you still have to use several plugins in order to fully prepare a model for exporting. Instead of doing this, I want to explicitly write out a series of specific steps to get the model prepared.

- The process is going to be non-destructive. This means creating a copy of every object it needs to operate on before going through the preparation process. A nice side effect of this is that I can make as many prepared copies of the model as needed, in rapid succession no less.