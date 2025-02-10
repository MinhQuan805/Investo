
# <img src="https://github.com/MinhQuan805/Investo/blob/master/Demo/1.png?raw=true" alt="Image 2" width="150" >   -  A stock market web-based application.

### **Video Demo**: [YouTube Demo](https://youtu.be/TQCcaaUclTI)
### **Link**: [minhquan.pythonanywhere.com](https://minhquan.pythonanywhere.com/)

## **Description**
Investo is a web-based platform tailored for stock market enthusiasts, analysts, and investors of all levels. Designed with a user-centric approach, it provides powerful tools and features to enable users to make well-informed financial decisions. Its intuitive design and visually engaging interface simplify the complexity of stock market data, making it accessible to everyone from seasoned investors to beginners.

---

## **Demo**

<div align="center">
  <img src="https://github.com/MinhQuan805/Investo/blob/master/Demo/2.png?raw=true" alt="Image 2" width="800" height="400">
</div>

<div style="text-align: center;">
    <img src="https://github.com/MinhQuan805/Investo/blob/b33bc564a4cd2ad838a5b2055a2e02c4903cec70/Demo/5.png?raw=true" alt="Image 5" width="400">
    <img src="https://github.com/MinhQuan805/Investo/blob/b33bc564a4cd2ad838a5b2055a2e02c4903cec70/Demo/4.png?raw=true" alt="Image 4" width="400">
</div>

---

## **Features**
### **1. Profile**
<img src="https://github.com/MinhQuan805/Investo/blob/master/Demo/3.png?raw=true" alt="Image 3" width="400">
- Displays essential company details, including:
  - **Description**: A brief overview of the company.
  - **Industry and Sector**: Categorization of the company within the economy.
  - **Executives**: Key leadership roles within the company.
  - **Headquarters Location**: Geographic details about the company's base.

### **2. News**
- Aggregates and presents the latest stock-related news articles from reputable financial outlets.

### **3. Chart**
- Offers a visual price chart with tools for:
  - **Technical Analysis**: Supports various indicators to analyze trends.
  - **Customizable Time Frames**: View price data across different periods.

### **4. Historical Data**
- Provides access to past stock prices and trading volume:
  - Choose time frames: **daily**, **weekly**, or **monthly**.

### **5. Financials**
- Displays financial reports such as:
  - Revenue.
  - Profit.
  - Cash flow across accounting periods.

### **6. Analysis**
- Shows insights from analysts, including:
  - **Price Targets**: Expected future price ranges.
  - **Stock Ratings**: Analyst recommendations (e.g., buy, hold, sell).

---

## **Files and Project Structure**

### **1. Application Files**
- **`app.py`**:
  - The main backend script built with Flask.
  - Handles routes and integrates APIs for fetching stock data.
  - Manages logic for rendering pages and processing user inputs.

- **`templates/`**:
  - Contains HTML files for all web pages, including:
    - `home.html`: Homepage with a search bar and general information.
    - `index.html`: Started Menu.
    - `profile.html`: Displays company details.
    - `chart.html`: Displays the interactive price chart.
    - `financials.html`: Shows financial reports.
    - `news.html`: Presents financial news articles.
    - `history.html`: Provides access to past stock prices and trading volume.

- **`static/`**:
  - `style.css`: Custom styles for the UI.

### **2. Data Integration**
- Utilizes the **YFinance** library to fetch live and historical stock data.
- Processes data using **Pandas** for efficient manipulation and analysis.


## **Design Choices**

### **1. Simplicity and Usability**
- The design prioritizes ease of use, ensuring even beginners can navigate the platform without confusion.
- A clean interface reduces cognitive load while providing actionable insights.

### **2. Data Efficiency**
- APIs are queried only when necessary to minimize redundant data retrieval.
- Implemented caching mechanisms to improve performance and reduce latency.

### **3. Scalable Architecture**
- Modularized backend logic to enable future feature additions, such as portfolio tracking and live chat.
- Integrated responsive design principles, ensuring usability across devices (desktop, tablet, mobile).

---

## **Challenges and Design Considerations**

- **API Selection**: Choosing APIs that are both comprehensive and free for public use required extensive research.
- **Data Overload**: To avoid overwhelming users, the platform provides filters for customizing displayed data.
- **Technical Analysis**: Balancing advanced chart features with simplicity involved iterative testing and feedback.

---

## **Conclusion**
Investo is a reliable and robust solution for anyone looking to dive into the stock market. By combining advanced analytics, news aggregation, and a user-friendly interface, it bridges the gap between complex data and actionable insights, empowering users in their financial journey.
