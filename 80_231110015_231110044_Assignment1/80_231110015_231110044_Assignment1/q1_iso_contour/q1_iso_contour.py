import vtk

# Find intersection point of horizontal active edge
#######################################
def marchingx(c, v1, v2, pid1, pid2,data):
    p1 = data.GetPoint(pid1)
    p2 = data.GetPoint(pid2)
    p = (v1-c)*(p2[0]-p1[0])/(v1-v2) + p1[0]
    return (p,p1[1],p1[2])

# Find intersection point of vertical active edge
#######################################
def marchingy(c, v1, v2, pid1, pid2,data):
    p1 = data.GetPoint(pid1)
    p2 = data.GetPoint(pid2)
    p = (v1-c)*(p2[1]-p1[1])/(v1-v2) + p1[1]
    return (p1[0],p,p1[2])

def marching(data):
    # c is the pressure value for iso-contour
    #######################################
    c = float(input("Enter the pressure value for iso-contour:"))
    
    # Query how many cells the dataset has
    #######################################
    numCells = data.GetNumberOfCells()
    
    # object for storing 3D points obtained while marching
    points = vtk.vtkPoints()
    # Object for storing line segments created while marching 
    lines = vtk.vtkCellArray()

    # march all the cells inside data set
    for i in range(0,numCells):

        # Get a single cell from the list of cells
        cell = data.GetCell(i) ## cell index = i

        # Query the ids of 4 corner points of the cell
        pid1 = cell.GetPointId(0)
        pid2 = cell.GetPointId(1)
        pid3 = cell.GetPointId(3)
        pid4 = cell.GetPointId(2)
        
        # Get values at each vertex
        # First Get the array
        dataArr = data.GetPointData().GetArray('Pressure')
        val1 = dataArr.GetTuple1(pid1)
        val2 = dataArr.GetTuple1(pid2)
        val3 = dataArr.GetTuple1(pid3)
        val4 = dataArr.GetTuple1(pid4)

        # this list will store iso-contour point on active edges
        arr = []

        #checking all 4 edges in counter clockwise for iso-contour point
        if val1>c and val2<c or val1<c and val2>c: 
            p = marchingx(c,val1,val2,pid1,pid2,data)
            arr.append(p)
        if val2>c and val3<c or val2<c and val3>c:
            p = marchingy(c,val2,val3,pid2,pid3,data)
            arr.append(p)
        if val3>c and val4<c or val3<c and val4>c:
            p = marchingx(c,val3,val4,pid3,pid4,data)
            arr.append(p)
        if val4>c and val1<c or val4<c and val1>c:
            p = marchingy(c,val4,val1,pid4,pid1,data)
            arr.append(p)
            
        if len(arr)==0: continue # do not add the cases where less than or more than 2 active edges
            
        # For exactly 2 active edges add 2 corresponding points in 3D iso-contour point collection
        pt_id1 = points.InsertNextPoint(arr[0])
        pt_id2 = points.InsertNextPoint(arr[1])

        line = vtk.vtkLine()
        line.GetPointIds().SetId(0,pt_id1)
        line.GetPointIds().SetId(1,pt_id2)
        lines.InsertNextCell(line)

        if len(arr) == 4:
            pt_id1 = points.InsertNextPoint(arr[2])
            pt_id2 = points.InsertNextPoint(arr[3])
            # creat line for above 2 points and add in the collection of iso-contour lines
            line = vtk.vtkLine()
            line.GetPointIds().SetId(0,pt_id1)
            line.GetPointIds().SetId(1,pt_id2)
            lines.InsertNextCell(line)

    # Once all the cells are traversed, create polydata object
    polydata = vtk.vtkPolyData()
    polydata.SetPoints(points)
    polydata.SetLines(lines)
    
    return polydata

def main():

    # Load data
    #######################################
    reader = vtk.vtkXMLImageDataReader()
    reader.SetFileName('Isabel_2D.vti')
    reader.Update()
    data = reader.GetOutput()
    
    # created polydata object for storing result of marching algorithm
    polydata = vtk.vtkPolyData()
    polydata = marching(data)
    
    # Write above polydata object in a vtp file named as onecell.vtp
    writer = vtk.vtkXMLPolyDataWriter()
    writer.SetInputData(polydata)
    writer.SetFileName('onecell.vtp')
    writer.Write()
    
if __name__ == "__main__":
    # Call the main function if this script is being run directly
    main()
