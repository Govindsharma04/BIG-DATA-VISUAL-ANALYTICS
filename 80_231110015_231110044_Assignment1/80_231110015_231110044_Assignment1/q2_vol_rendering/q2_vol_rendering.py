import vtk

# Defining a function which is creating Color Transfer Function
def Color_TransFunction():
    CTF = vtk.vtkColorTransferFunction() # vtkCTF object
    CTF.AddRGBPoint(-4931.54, 0, 1, 1)  # here we are using ctf object to assign RGB value to the position
    CTF.AddRGBPoint(-2508.95, 0, 0, 1)
    CTF.AddRGBPoint(-1873.9, 0, 0, 0.5)
    CTF.AddRGBPoint(-1027.16, 1, 0, 0)
    CTF.AddRGBPoint(-298.031, 1, 0.4, 0)
    CTF.AddRGBPoint(2594.97, 1, 1, 0)
    return CTF

# Defining a function which is creating Opacity Transfer Function
def Opacity_TransFunction():
    opacity_transfer_function = vtk.vtkPiecewiseFunction()
    opacity_transfer_function.AddPoint(-4931.54, 1.0) # here also we are assigning opacity to the position 
    opacity_transfer_function.AddPoint(101.815, 0.002)
    opacity_transfer_function.AddPoint(2594.97, 0.0)
    return opacity_transfer_function

# Defining Function for creaating Volume
def create_volume(reader, CTF, OTF):
    # Create volume property
    volume_property = vtk.vtkVolumeProperty()
    # Set color and scalar opacity transfer functions
    volume_property.SetColor(CTF)
    volume_property.SetScalarOpacity(OTF)

    # Use vtkSmartVolumeMapper for volume rendering
    volume_mapper = vtk.vtkSmartVolumeMapper()
    volume_mapper.SetInputConnection(reader.GetOutputPort())

    # Creating volume
    vol = vtk.vtkVolume()  # volume object
    vol.SetMapper(volume_mapper)
    vol.SetProperty(volume_property)

    return vol

# Load the 3D data, ensuring file extension matches your input
reader = vtk.vtkXMLImageDataReader()
reader.SetFileName('Isabel_3D.vti')  # Replace with your actual file path
reader.Update()

# Creating color transfer function
CTF = Color_TransFunction()

# Creating opacity transfer function
OTF = Opacity_TransFunction()

# Creating volume
vol = create_volume(reader, CTF, OTF)

# Implement Phong shading based on user input
use_phong_shading = input("Do you want to use Phong shading (Y/N)?: ")
if use_phong_shading.lower() == 'y':
    volume_property = vol.GetProperty()
    volume_property.ShadeOn()
    # Set ambient, diffuse, and specular coefficients as given in question
    volume_property.SetAmbient(0.5)
    volume_property.SetDiffuse(0.5)
    volume_property.SetSpecular(0.5)

# Adding outline to volume-rendered data 
outline = vtk.vtkOutlineFilter()
outline.SetInputConnection(reader.GetOutputPort())

# Creating a mapper for the outline
outline_mapper = vtk.vtkPolyDataMapper()
outline_mapper.SetInputConnection(outline.GetOutputPort())

outline_actor = vtk.vtkActor()
outline_actor.SetMapper(outline_mapper)
outline_actor.GetProperty().SetColor(0, 0, 0)  # Set outline color to black

# Creating renderer, render window, interactor and setting background to while
renderer = vtk.vtkRenderer()
renderer.SetBackground(1, 1, 1) 
renderer.AddVolume(vol)
renderer.AddActor(outline_actor)  

# Creating a render window and Setting its to 1000x1000 pixels
render_window = vtk.vtkRenderWindow()
render_window.SetSize(1000, 1000)
render_window.AddRenderer(renderer)
# Create a render window interactor and setting it for render Window
render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)
# Rendering the scene and start the event loop for user interaction
render_window.Render()
render_window_interactor.Start()
