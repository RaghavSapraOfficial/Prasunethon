import requests
import csv

def fetch_and_save_data(api_url, csv_filename):
    # Make API request
    response = requests.get(api_url)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()  # Convert response to JSON format
        
        # Writing data to CSV file
        with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['title', 'description']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            for item in data:
                writer.writerow({'title': item['title'], 'description': item['description']})
                
        print(f'Data saved to {csv_filename}')
    else:
        print(f'Error fetching data. Status code: {response.status_code}')

# Example usage:
if __name__ == '__main__':
    api_url = 'https://mentalhealthapi.com/api/v1/resources'
    csv_filename = 'mental_health_resources.csv'
    fetch_and_save_data(api_url, csv_filename)
