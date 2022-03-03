import os
ROOT = os.path.dirname(__file__)
proect_name = 'pythonProject3'
paths = [os.path.join(proect_name, 'settings'), os.path.join(proect_name, 'mainapp'),
         os.path.join(proect_name, 'adminapp'),
         os.path.join(proect_name, 'avtapp')]
for _path in paths:
    os.makedirs(os.path.join(ROOT, _path), exist_ok=True)
    