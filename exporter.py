import bpy
CYCLES = bpy.context.scene.cycles
RENDER = bpy.context.scene.render

# HIDE VERTICES
def concealVertices(mesh: bpy.types.Mesh, vertices: list[int]) -> None:
	return

# CAPTURES
class capturedMeshShape():
	def __init__(self, fromMesh: bpy.types.Mesh):
		return

	def apply(self, toMesh: bpy.types.Mesh) -> None:
		return

class capturedRenderSettings():
	def __init__(self):
		self.engine = RENDER.engine
		self.resX = RENDER.resolution_x
		self.resY = RENDER.resolution_y
		self.resPercent = RENDER.resolution_percentage
		self.samples = RENDER.bake_samples
		self.useMotionBlur = RENDER.use_motion_blur
		self.featureSet = CYCLES.feature_set
		self.device = CYCLES.device

	def apply(self) -> None:
		RENDER.engine = self.engine
		RENDER.resolution_x = self.resX
		RENDER.resolution_y = self.resY
		RENDER.resolution_percentage = self.resPercent
		RENDER.bake_samples = self.samples
		RENDER.use_motion_blur = self.useMotionBlur
		CYCLES.feature_set = self.featureSet
		CYCLES.device = self.device
	
class bakeController():
	def __init__(self):
		self.isPrepared = False

	def prepare(self) -> None:
		self.capturedSettings = capturedRenderSettings()
		RENDER.engine = "CYCLES"
		self.isPrepared = True

	def bake(self) -> None:
		if not self.isPrepared: self.prepare()
		bpy.ops.object.bake()

	def finish(self) -> None:
		if self.capturedSettings: self.capturedSettings.apply()
		self.isPrepared = False

def saveMeshShapekey(mesh: bpy.types.Mesh, name: str) -> None:
	return

# BAKE CHANNEL
class IBakeChannel():
	def set(self, to: int) -> None: return

class bakeChannelImpl(IBakeChannel):
	def __init__(self, path):
		return
	
	def set(self, to: int) -> None:
		return

# BAKE TARGET TEXTURE
class ITexture():
	def setAsTarget(self) -> None: return
	def downscale(self, by: int): return self

class textureImpl(ITexture):
	def __init__(self, fromTexture, nodePaths):
		return

	def setAsTarget(self) -> None:
		return

	def downscale(self, by: int) -> ITexture:
		return self