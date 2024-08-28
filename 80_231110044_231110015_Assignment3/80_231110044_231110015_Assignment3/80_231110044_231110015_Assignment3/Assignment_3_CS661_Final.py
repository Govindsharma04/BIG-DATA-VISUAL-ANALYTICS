import vtk
import numpy as np

# Load vector field dataset
reader = vtk.vtkXMLImageDataReader()
reader.SetFileName("./tornado3d_vector.vti")  # Provide the filename of your VTI file
reader.Update()
data = reader.GetOutput()

# Get the bounds of the vector field dataset
bounds = data.GetBounds()

# Interpolate vector at current point using VTKProbeFilter
def get_velocity(current_point):
    probe = vtk.vtkProbeFilter()
    points = vtk.vtkPoints()
    points.InsertNextPoint(current_point)  
    polydata = vtk.vtkPolyData()
    polydata.SetPoints(points)
    probe.SetInputData(polydata)
    probe.SetSourceData(data)
    probe.SetSpatialMatch(1)
    probe.Update()
    inter_value = probe.GetOutput().GetPointData().GetArray("vectors").GetTuple3(0)
    return inter_value

# RK4 integration function
def rk4_integration(seed_point, step_size, max_steps):
    streamline_points = []
    current_point = seed_point
    
    for _ in range(max_steps):
        current_point_ar = np.array(current_point)
        a = step_size * np.array(get_velocity(current_point_ar))
        b = step_size * np.array(get_velocity(current_point_ar + a / 2))
        c = step_size * np.array(get_velocity(current_point_ar + b / 2))
        d = step_size * np.array(get_velocity(current_point_ar + c))
        next_point = current_point + (a + 2 * b + 2 * c + d) / 6

        # check if the point calculated by integration is within bounds
        if not all(bounds[i*2] <= p <= bounds[i*2+1] for i, p in enumerate(next_point)):
            break
        streamline_points.append(next_point)
        current_point = next_point
    return streamline_points

def streamline_tracer():
    # User-provided seed location
    seed_location = np.array([float(x) for x in input("Enter seed location (x y z): ").split()])  
    # Integration parameters
    step_size = 0.05
    max_steps = 1000
    
    forward_streamline = rk4_integration(seed_location, step_size, max_steps)
    backward_streamline = rk4_integration(seed_location, -step_size, max_steps)
    streamline_points = list(reversed(backward_streamline)) + [seed_location] + forward_streamline

    # create streamline vtp file
    points = vtk.vtkPoints()
    lines = vtk.vtkCellArray()
    
    for i, point in enumerate(streamline_points):
        points.InsertNextPoint(point)
        if i < len(streamline_points) - 1:
            line = vtk.vtkLine()
            line.GetPointIds().SetId(0, i)
            line.GetPointIds().SetId(1, i+1)
            lines.InsertNextCell(line)
    
    polydata = vtk.vtkPolyData()
    polydata.SetPoints(points)
    polydata.SetLines(lines)
    
    # Write the streamline to a VTP file
    writer = vtk.vtkXMLPolyDataWriter()
    writer.SetFileName("streamline_data.vtp")
    writer.SetInputData(polydata)
    writer.Write()

if __name__ == "__main__":
    streamline_tracer()