```python
Big Data Analytics (CS661)
Assignment 3

Sanjeev Kumar 231110044
Govind Sharma 231110015

Place python script and dataset in same location

install vtk and numpy if not installed already using below commands:

!pip install numpy
!pip install vtk

run the code, you will get the below prompt:
Enter seed location (x y z):
    -> you have to enter three space separated float/int values. Ex: 0 0 7(as given in the assignment)
    -> press enter

This will save the streamline_data.vtp file in same location.

Load this vtp file in paraview and visualize. 


Workflow of the Code:
    -> Load the dataset and calculate bounds.
    -> get_velocity(current_point) : returns interpolated velocity vector at given point
    -> rk4_integration(seed_point, step_size, max_step): calculates points of the streamline given seed_point and required integration parameters.
    -> streamline_tracer(): takes seed_location from user.
                            calculates forward and backward streamline points from that seed location.
                            converts these points into vtk polydata object and write this object in a file named "streamline_data.vtp"

```


