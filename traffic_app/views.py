from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .utils import detect_and_annotate

def index(request):
    return render(request, 'index.html')

def upload_page(request):
    return render(request, 'uploadfile.html')

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        
        # 1. Save the uploaded file locally
        fs = FileSystemStorage(location='media/uploads')
        filename = fs.save(uploaded_file.name, uploaded_file)
        uploaded_path = fs.path(filename)

        # 2. Run the YOLO logic from utils.py
        output_filename, vehicle_counts = detect_and_annotate(uploaded_path, filename)

        # 3. Prepare detection data for the HTML template
        total_objects = sum(vehicle_counts.values())
        total_vehicles = sum(count for label, count in vehicle_counts.items() if label != 'person')
        total_pedestrians = vehicle_counts.get('person', 0)

        context = {
            'image_url': f"/media/processed/{output_filename}",
            'objects': [{'id': f"Object {i+1}", 'category': label} 
                        for i, (label, count) in enumerate(vehicle_counts.items()) for _ in range(count)],
            'total_pedestrians': total_pedestrians,
            'total_vehicles': total_vehicles,
            'total_objects': total_objects,
            'traffic_state': "Dense" if total_vehicles >= 5 else "Less Dense"
        }
        return render(request, 'results.html', context)
    
    return render(request, 'uploadfile.html')