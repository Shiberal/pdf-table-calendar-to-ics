import csv
from ics import Calendar, Event
from datetime import datetime, timedelta

def csv_to_ics(input_csv, output_ics='output.ics'):
    cal = Calendar()

    with open(input_csv, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header if it exists

        for row in reader:
            #map the row 
            #event date is 21/12/2023, 
            event_date = datetime.strptime(row[1], '%d/%m/%Y')
            #replace , with : to get  9,00 to 9:00
            start_time = datetime.strptime(row[2].replace(",",":"), '%H:%M')
            end_time = datetime.strptime(row[3].replace(",",":"), '%H:%M')
            subject = row[5]
            location = row[7]
            organizer = row[8]

            #replace in event date the day
            #event_date = event_date.replace(day=event_date.day-1)

            # Create 
            event = Event()
            event.name = subject + " con " +organizer;
            event.organizer = organizer;
            event.location = location;
            event.begin = event_date.replace(hour=(start_time.hour -1), minute=start_time.minute)
            event.end = event_date.replace(hour=(end_time.hour-1), minute=end_time.minute)
            cal.events.add(event)
            
    # Save the calendar to an iCalendar file
    with open(output_ics, 'w') as f:
        f.writelines(cal)

    print(f"iCalendar file saved to {output_ics}")

if __name__ == "__main__":
    # Replace 'input.csv' with the path to your CSV file
    input_csv = './pruned.csv'
    
    # Replace 'output.ics' with the desired output iCalendar file
    output_ics = 'output.ics'
    
    csv_to_ics(input_csv, output_ics)
