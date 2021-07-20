from datetime import datetime

def get_filename(filename, request):
    return filename.upper() + '_' + datetime.now().strftime("%m%d%y%H%M%S")
