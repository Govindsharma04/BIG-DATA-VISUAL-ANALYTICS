Big Data Analytics (CS661)
Assignment 1

Sanjeev Kumar 231110044
Govind Sharma 231110015

Question 1:

	Python Package required: vtk
	Functions Used:
		1) marchingx(c, v1, v2, pid1, pid2,data) -> returns the intersection point on horizontal edge of a cell. c is the iso-value, v1 and v2 are the pressure values at the two ends of the edge, pid1 and pid2 are the point ids of the two ends of the edge.
		2) marchingy(c, v1, v2, pid1, pid2,data) -> returns the intersection point on verticle active edge of the cell.
		3) marching(data) -> takes all the points in data set and iterates all the cells sequentially and finds the iso-contour points calling above two functions as and when required. These iso-countour points and iso-contour lines as collected in two variable "points" and "lines". Once all the cells are traversed, these two variables are passed to vtkPolyData() object and returned to main() function.
		4) main() -> this loads the dataset and calls the marching(data) function. output of marching(data) function is then saved in a vtp file named "onecell.vtp".
	
	Instructions to visualize in PARAVIEW:
		1) load this onecell.vtp file in paraview and load actual dataset as well.
		2) apply contour filter on actual data set and turn off the visibility of actual data set.
		3) at same value of the iso-contour parameter, contour of actual data and onecell.vtp will almost coincide (differs for ambiguos cells only).
		4) For a new value of iso-contour, re_run the python script and refresh the onecell vtp in PARAVIEW.

Question 2:
	
	Python Pakage Required: VTK
	Function Used:
		1) Color_TransFunction() -> returns a vtkColorTransferFunction object representing the color transfer function for volume rendering.
		2) Opacity_TransFunction() -> returns a vtkPiecewiseFunction object representing the opacity transfer function for volume rendering.
		3) create_volume(reader, CTF, OTF) -> Creates a volume object using the provided reader, Color Transfer Function (CTF), and Opacity Transfer Function (OTF).
		4) main() -> Loads the dataset, creates the color and opacity transfer functions, creates the volume, and implements Phong shading based on user input. Renders the volume with an optional outline and starts the render window interactor loop.
		

		1) Load the dataset's (Isabel_3D.vti) correct path in our .py file for Question 2.
		2) Run the Python script and provide input for Phong shading (Y/N) means Yes and No respectively.
		3) The volume rendering with or without Phong shading will be displayed in Visualization Toolkit.

