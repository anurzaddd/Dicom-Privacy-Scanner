import os
import pydicom
from pydicom.errors import InvalidDicomError
import csv
import argparse
from datetime import datetime

def scan_dicom_file(file_path):
    try:
        ds = pydicom.dcmread(file_path, force=True)
        tags_of_interest = {
            'PatientName': (0x0010, 0x0010),
            'PatientID': (0x0010, 0x0020),
            'PatientBirthDate': (0x0010, 0x0030),
            'PatientSex': (0x0010, 0x0040),
        }
        results = {'file': file_path}
        for name, tag in tags_of_interest.items():
            if tag in ds:
                results[name] = str(ds[tag].value)
            else:
                results[name] = 'N/A'
        return results
    except InvalidDicomError:
        return {'file': file_path, 'error': 'Not a valid DICOM file'}
    except Exception as e:
        return {'file': file_path, 'error': str(e)}

def scan_folder(folder_path, output_csv):
    all_results = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.dcm'):
                full_path = os.path.join(root, file)
                print(f"[+] Scanning: {full_path}")
                result = scan_dicom_file(full_path)
                all_results.append(result)
    
    # Write to CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['file', 'PatientName', 'PatientID', 'PatientBirthDate', 'PatientSex', 'error']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in all_results:
            writer.writerow(row)
    
    print(f"[+] Report saved to {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DICOM PHI Privacy Scanner for Hospitals')
    parser.add_argument('path', help='Folder containing DICOM files')
    parser.add_argument('--output', default='phi_report.csv', help='Output CSV file')
    args = parser.parse_args()
    
    scan_folder(args.path, args.output)
