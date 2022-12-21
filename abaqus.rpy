# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2017 replay file
# Internal Version: 2016_09_27-23.54.59 126836
# Run by t.beinert on Tue Nov 21 11:43:32 2017
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=372.702575683594, 
    height=218.722229003906)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
sys.path.append(r'd:\Simulia\plug-ins\2017\nitinolSuperElastPlast')
from nitinolSuperelasticPlasticBehavior import NitinolSuperelasticPlasticBehavior
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.ModelFromInputFile(name='FilamentFigure', 
    inputFileName='C:/Users/t.beinert/Documents/HybMan/Programs/convertGCode_MULTI/FilamentFigure.inp')
#: The model "FilamentFigure" has been created.
#: The part "BEAM" has been imported from the input file.
#: 
#: WARNING: The following keywords/parameters are not yet supported by the input file reader:
#: ---------------------------------------------------------------------------------
#: *PREPRINT
#: The model "FilamentFigure" has been imported from an input file. 
#: Please scroll up to check for error and warning messages.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['FilamentFigure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=411.072, 
    farPlane=585.662, width=369.664, height=159.152, cameraPosition=(335.152, 
    170.097, 427.551), cameraUpVector=(-0.348479, 0.838913, -0.418076), 
    cameraTarget=(106.383, 59.2704, -2.34299))
session.viewports['Viewport: 1'].view.setValues(nearPlane=442.618, 
    farPlane=549.81, width=398.033, height=171.366, cameraPosition=(104.383, 
    -134.274, 457.712), cameraUpVector=(0.0363869, 0.99757, 0.0594086), 
    cameraTarget=(106.874, 59.9177, -2.40712))
session.viewports['Viewport: 1'].view.setValues(nearPlane=406.511, 
    farPlane=584.405, width=365.564, height=157.387, cameraPosition=(-2.20427, 
    -232.767, 387.073), cameraUpVector=(0.141312, 0.93728, 0.318648), 
    cameraTarget=(107.564, 60.5553, -1.94985))
session.viewports['Viewport: 1'].view.setValues(nearPlane=417.456, 
    farPlane=579.142, width=375.407, height=161.625, cameraPosition=(189.047, 
    -226.872, 397.897), cameraUpVector=(0.173617, 0.956381, 0.234931), 
    cameraTarget=(106.032, 60.5081, -2.03653))
session.viewports['Viewport: 1'].view.setValues(nearPlane=441.491, 
    farPlane=555.107, width=37.9705, height=16.3475, viewOffsetX=61.8131, 
    viewOffsetY=47.0421)
session.viewports['Viewport: 1'].view.setValues(nearPlane=417.067, 
    farPlane=524.901, width=35.8699, height=15.4431, cameraPosition=(11.4297, 
    -174.507, 399.635), cameraUpVector=(0.276947, 0.936154, 0.216602), 
    cameraTarget=(104.929, 73.589, -23.6046), viewOffsetX=58.3935, 
    viewOffsetY=44.4396)
session.viewports['Viewport: 1'].view.setValues(nearPlane=391.858, 
    farPlane=522.997, width=33.7018, height=14.5097, cameraPosition=(-119.201, 
    -27.2647, 395.855), cameraUpVector=(0.660017, 0.72722, 0.188489), 
    cameraTarget=(103.01, 110.288, -29.7351), viewOffsetX=54.864, 
    viewOffsetY=41.7535)
session.viewports['Viewport: 1'].view.setValues(nearPlane=432.724, 
    farPlane=518.531, width=37.2165, height=16.0229, cameraPosition=(-45.2911, 
    20.2558, 454.62), cameraUpVector=(0.625002, 0.78007, -0.029391), 
    cameraTarget=(98.4058, 100.77, -16.8604), viewOffsetX=60.5857, 
    viewOffsetY=46.1079)
session.viewports['Viewport: 1'].view.setValues(nearPlane=432.468, 
    farPlane=518.786, width=37.1946, height=16.0134, cameraPosition=(-42.2791, 
    0.580318, 452.178), cameraUpVector=(0.448307, 0.891571, -0.0642028), 
    cameraTarget=(101.418, 81.0945, -19.3024), viewOffsetX=60.5499, 
    viewOffsetY=46.0807)
session.viewports['Viewport: 1'].view.setValues(nearPlane=437.777, 
    farPlane=520.582, width=37.6512, height=16.21, cameraPosition=(9.17879, 
    -71.4644, 453.383), cameraUpVector=(0.380634, 0.924624, 0.0137158), 
    cameraTarget=(101.078, 77.6877, -14.3065), viewOffsetX=61.2932, 
    viewOffsetY=46.6464)
session.viewports['Viewport: 1'].view.setValues(nearPlane=437.744, 
    farPlane=520.616, width=37.6483, height=16.2088, cameraPosition=(12.9734, 
    -80.9461, 451.105), cameraUpVector=(0.276633, 0.960963, 0.00486902), 
    cameraTarget=(104.873, 68.206, -16.5847), viewOffsetX=61.2885, 
    viewOffsetY=46.6428)
session.viewports['Viewport: 1'].view.setValues(nearPlane=438.598, 
    farPlane=519.761, width=24.4618, height=10.5316, viewOffsetX=62.5374, 
    viewOffsetY=47.0611)
session.viewports['Viewport: 1'].view.setValues(nearPlane=427.493, 
    farPlane=523.362, width=23.8424, height=10.2649, cameraPosition=(40.5751, 
    -184.139, 404.514), cameraUpVector=(0.199309, 0.958439, 0.204135), 
    cameraTarget=(107.223, 66.5887, -22.2401), viewOffsetX=60.954, 
    viewOffsetY=45.8696)
session.viewports['Viewport: 1'].view.setValues(nearPlane=421.496, 
    farPlane=525.195, width=23.5079, height=10.1209, cameraPosition=(49.5811, 
    -228.78, 372.064), cameraUpVector=(0.287359, 0.903847, 0.316994), 
    cameraTarget=(103.039, 75.9182, -20.0162), viewOffsetX=60.0989, 
    viewOffsetY=45.2261)
session.viewports['Viewport: 1'].view.setValues(nearPlane=421.286, 
    farPlane=525.405, width=28.4045, height=12.229, viewOffsetX=61.2183, 
    viewOffsetY=45.5017)
session.viewports['Viewport: 1'].view.setValues(nearPlane=388.305, 
    farPlane=527.534, width=26.1809, height=11.2717, cameraPosition=(-40.9864, 
    -210.479, 342.261), cameraUpVector=(0.39089, 0.837744, 0.3813), 
    cameraTarget=(103.189, 90.192, -29.5393), viewOffsetX=56.4258, 
    viewOffsetY=41.9395)
session.viewports['Viewport: 1'].view.setValues(nearPlane=408.545, 
    farPlane=527.207, width=27.5456, height=11.8592, cameraPosition=(34.1166, 
    -258.786, 336.161), cameraUpVector=(0.352023, 0.842045, 0.408705), 
    cameraTarget=(101.148, 84.1076, -20.7076), viewOffsetX=59.3669, 
    viewOffsetY=44.1256)
session.viewports['Viewport: 1'].view.setValues(nearPlane=409.071, 
    farPlane=526.68, width=17.8857, height=7.70035, viewOffsetX=59.6112, 
    viewOffsetY=43.9153)
session.viewports['Viewport: 1'].view.setValues(nearPlane=418.651, 
    farPlane=525.239, width=18.3046, height=7.88068, cameraPosition=(43.7406, 
    -232.465, 366.497), cameraUpVector=(0.36018, 0.871062, 0.333948), 
    cameraTarget=(100.588, 82.2189, -17.1256), viewOffsetX=61.0072, 
    viewOffsetY=44.9437)
session.viewports['Viewport: 1'].view.setValues(nearPlane=433.92, 
    farPlane=523.669, width=18.9722, height=8.16813, cameraPosition=(73.0515, 
    -214.919, 391.618), cameraUpVector=(0.345207, 0.900289, 0.265166), 
    cameraTarget=(100.395, 78.3104, -11.7346), viewOffsetX=63.2322, 
    viewOffsetY=46.5829)
session.viewports['Viewport: 1'].view.setValues(nearPlane=467.366, 
    farPlane=521.646, width=20.4346, height=8.79772, cameraPosition=(111.605, 
    -107.911, 466.199), cameraUpVector=(0.277396, 0.960754, 0.00176969), 
    cameraTarget=(102.153, 68.9531, -0.763264), viewOffsetX=68.1061, 
    viewOffsetY=50.1735)
session.viewports['Viewport: 1'].view.setValues(nearPlane=467.68, 
    farPlane=545.028, width=20.4483, height=8.80365, cameraPosition=(177.744, 
    -102.592, 474.33), cameraUpVector=(0.216985, 0.975235, -0.042828), 
    cameraTarget=(104.286, 64.0315, 9.28794), viewOffsetX=68.1519, 
    viewOffsetY=50.2072)
session.viewports['Viewport: 1'].view.setValues(nearPlane=467.444, 
    farPlane=533.474, width=20.438, height=8.79921, cameraPosition=(144.591, 
    -105.163, 471.492), cameraUpVector=(0.25043, 0.967869, -0.0226756), 
    cameraTarget=(102.948, 66.67, 4.41315), viewOffsetX=68.1176, 
    viewOffsetY=50.1819)
session.viewports['Viewport: 1'].view.setValues(nearPlane=467.414, 
    farPlane=533.504, width=22.1895, height=9.55329, viewOffsetX=68.3007, 
    viewOffsetY=50.736)
session.viewports['Viewport: 1'].view.setValues(nearPlane=455.968, 
    farPlane=520.331, width=21.6461, height=9.31935, cameraPosition=(91.3867, 
    -141.372, 445.724), cameraUpVector=(0.351186, 0.932224, 0.0873323), 
    cameraTarget=(99.9364, 76.0956, -3.78516), viewOffsetX=66.6281, 
    viewOffsetY=49.4936)
session.viewports['Viewport: 1'].view.setValues(nearPlane=468.379, 
    farPlane=519.521, width=22.2353, height=9.57301, cameraPosition=(103.178, 
    -94.6295, 470.575), cameraUpVector=(0.367398, 0.929896, -0.0176761), 
    cameraTarget=(99.369, 76.9852, 1.57877), viewOffsetX=68.4416, 
    viewOffsetY=50.8408)
session.viewports['Viewport: 1'].view.setValues(nearPlane=469.141, 
    farPlane=518.759, width=10.5995, height=4.5634, viewOffsetX=70.3344, 
    viewOffsetY=51.6122)
session.viewports['Viewport: 1'].view.setValues(nearPlane=453.059, 
    farPlane=519.35, width=10.2361, height=4.40697, cameraPosition=(72.6731, 
    -123.301, 450.871), cameraUpVector=(0.400012, 0.914091, 0.0665444), 
    cameraTarget=(98.8028, 80.522, -4.31823), viewOffsetX=67.9234, 
    viewOffsetY=49.843)
session.viewports['Viewport: 1'].view.setValues(nearPlane=452.494, 
    farPlane=519.915, width=17.1973, height=7.40397, viewOffsetX=68.3288, 
    viewOffsetY=49.8924)
session.viewports['Viewport: 1'].view.setValues(nearPlane=462.497, 
    farPlane=557.772, width=17.5775, height=7.56765, cameraPosition=(207.997, 
    -117.485, 467.105), cameraUpVector=(0.305915, 0.95113, -0.0420342), 
    cameraTarget=(102.062, 71.733, 17.2179), viewOffsetX=69.8394, 
    viewOffsetY=50.9954)
session.viewports['Viewport: 1'].view.setValues(nearPlane=476.328, 
    farPlane=535.235, width=18.1032, height=7.79398, cameraPosition=(154.595, 
    -59.2353, 489.918), cameraUpVector=(0.265859, 0.956357, -0.121249), 
    cameraTarget=(102.429, 68.4836, 9.92733), viewOffsetX=71.928, 
    viewOffsetY=52.5205)
session.viewports['Viewport: 1'].view.setValues(nearPlane=476.29, 
    farPlane=535.274, width=18.1018, height=7.79337, cameraPosition=(153.795, 
    -56.9914, 490.602), cameraUpVector=(0.290402, 0.948575, -0.125987), 
    cameraTarget=(101.629, 70.7275, 10.6114), viewOffsetX=71.9223, 
    viewOffsetY=52.5163)
session.viewports['Viewport: 1'].view.setValues(nearPlane=465.479, 
    farPlane=517.91, width=17.6909, height=7.61649, cameraPosition=(88.3546, 
    -91.2894, 469.117), cameraUpVector=(0.343889, 0.938908, -0.0138749), 
    cameraTarget=(100.196, 74.7214, -1.75965), viewOffsetX=70.2898, 
    viewOffsetY=51.3242)
