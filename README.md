
# Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit

The "Redbus Data Scraping and Filtering with Streamlit Application" aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.


## Tech Stack

**Web Scrapping using Selenium** 

**Server:** MySQL,Streamlit,python

**Data Analysis,Interactive Application**



## *Data Set Requirements and Explanation*

**The scraped dataset for this project should contain detailed information about bus services available on Redbus, covering various aspects critical to travelers and service providers. Here is a breakdown of the fields required:**

**Bus Routes Name:** This field captures the start and end locations of each bus journey, providing crucial information about the routes serviced.

**Bus Routes Link:** Link for all the route details.

**Bus Name:** The name of the bus or the service provider, which helps in identifying the specific operator.

**Bus Type (Sleeper/Seater/AC/Non-AC):** This field specifies whether the bus is a sleeper or seater type, indicating the seating arrangements and comfort level offered.

**Departing Time:** The scheduled departure time of the bus, essential for planning travel schedules.

**Duration:** The total duration of the journey from the departure point to the destination, helping passengers estimate travel time.

**Reaching Time:** The expected arrival time at the destination, allowing for better planning of onward travel or activities.

**Star Rating:** A rating provided by passengers, indicating the quality of service based on factors such as comfort, punctuality, and staff behavior.

**Price:** The cost of the ticket for the journey, which can vary based on factors like bus type and demand.

**Seat Availability:** The number of seats available at the time of data scraping, giving real-time insight into the occupancy levels.
# *Dataset References :*
### **Source:** 
Data will be scraped from the Redbus website.

**Link-** https://www.redbus.in/

**Format:** The scraped data will be stored in a SQL database.
Required Fields: Bus routes Link,Bus route Name, Bus name, Bus Type(Sleeper/Seater),  Departing Time, Duration, Reaching_Time, Star-rating, Price, Seat_availability.
## Deployment

To deploy this project run

```Streamlit
  streamlit run file_name.py
```

```MySQL
   pip install MySQL
   pip install mysql-python-connector
```

```
   pip install pandas
   pip install numpy
```

## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Normal Red Color | ![#e6152a](https://via.placeholder.com/10/0a192f?text=+) #e6152a |
| White Color | ![](https://via.placeholder.com/10/f8f8f8?text=+) #f0ffff |
| Green Color | ![#14c948](https://via.placeholder.com/10/00b48a?text=+) #14c948 |
| Light White Color | ![](https://via.placeholder.com/10/00b48a?text=+) #aeb5b0 |

