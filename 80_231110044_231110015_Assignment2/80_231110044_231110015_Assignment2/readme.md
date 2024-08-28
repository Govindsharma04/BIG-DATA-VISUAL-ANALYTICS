```python
Big Data Analytics (CS661)
Assignment 2

Sanjeev Kumar 231110044
Govind Sharma 231110015

Install below dependencies:
    vtk, plotly, ipywidgets

Load given data set and convert into numpy_array.
Encode this numpy_array as per format required by plotly graph_objects.
Create X,Y,Z axes of 3D mesh grid for mapping the given dataset values.

Create iso_surface object using plotly API and set the layout as required in assignment pdf.
Create histogram from the given data.

convert these objects in FigureWidget objects so as we can put them in widgets container.
make slider and reset_button as required.

Define update_isosurface and on_button_click functions for binding them with slider and reset button objects.

connect slider and reset_button to required functionality of updating isosurface and reset to default respectively.

Put slider and reset_button widget objects in a horizontal HBox container.
Put iso_fig and histogram figure in another horizontal HBox container.

Put both of the above containers in a vertical VBox conatainer.

Finally display the last container and we are ready with the required output.

```
