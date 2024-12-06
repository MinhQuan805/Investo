from flask import Flask, render_template, request, session, jsonify
import yfinance as yf
import pandas as pd
from datetime import datetime
from flask_session import Session
from helpers import apology
import random


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


quote = ["An investment in knowledge pays the best interest.",
        "Bottoms in the investment world don't end with four-year lows; they end with 10- or 15-year lows.",
        "Be fearful when others are greedy and greedy only when others are fearful.",
        "Given a 10% chance of a 100 times payoff, you should take that bet every time.",
        "Don't look for the needle in the haystack. Just buy the haystack!",
        "The stock market is filled with individuals who know the price of everything, but the value of nothing.",
        "In investing, what is comfortable is rarely profitable.",
        "How many millionaires do you know who have become wealthy by investing in savings accounts? I rest my case.",
        "Courage taught me no matter how bad a crisis gets ... any sound investment will eventually pay off.",
        "The individual investor should act consistently as an investor and not as a speculator."]
author = ["Benjamin Franklin", "Jim Rogers", "Warren Buffett", "Jeff Bezos", "John Bogle", "Phillip Fisher", "Robert Arnott", "Robert G. Allen", "Carlos Slim Helu", "Ben Graham"]
quotes = []
for i in range(len(quote)):
    quotes.append({"phrase": quote[i], "author": author[i]})

def time():
    current_time = datetime.now().time()

    open_time = datetime.strptime('09:30:00', '%H:%M:%S').time()
    close_time = datetime.strptime('16:00:00', '%H:%M:%S').time()

    if open_time <= current_time <= close_time:
        return True
    else:
        return False
def validate(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False
def price(symbol):
    ticker = yf.Ticker(symbol)
    current_price = ticker.info.get('currentPrice', None)

    if current_price is not None:
        return round(current_price, 2)
    data = ticker.history(period="1d")
    if not data.empty:
        return round(data['Open'].iloc[0], 2)

    return None


def change(symbol):
    ticker = yf.Ticker(symbol)
    interval = "1m" if time() else "1d"
    data = ticker.history(period="1d", interval=interval)

    if data.empty:
        return None, None

    try:
        open_price = data['Open'].iloc[0]
        close_price = data['Close'].iloc[-1]
        change = round(close_price - open_price, 2)
        percent = round((change / open_price) * 100, 2)
        return change, percent
    except IndexError:
        return None, None

@app.route("/", methods=["GET", "POST"])
def index():
    session['quotes'] = quotes
    return render_template("index.html")
@app.route("/home", methods=["GET", "POST"])
def home():
    session['ranNum'] = random.randint(0, 9)
    if 'count' not in session:
        session['count'] = 1

    if request.method == "POST":
        try:
            session['count'] = int(request.form.get("sector", 1))
        except ValueError:
            session['count'] = 1

    count = session['count']

    if count == 1:
        part1 = [
            {'name': 'NVIDIA Corporation', 'symbol': 'NVDA', 'price': price('NVDA'), 'change_price': change('NVDA')[0], 'percent': change('NVDA')[1]},
            {'name': 'Apple Inc.', 'symbol': 'AAPL', 'price': price('AAPL'), 'change_price': change('AAPL')[0], 'percent': change('AAPL')[1]},
            {'name': 'Microsoft Corporation', 'symbol': 'MSFT', 'price': price('MSFT'), 'change_price': change('MSFT')[0], 'percent': change('MSFT')[1]},
            {'name': 'Broadcom Inc.', 'symbol': 'AVGO', 'price': price('AVGO'), 'change_price': change('AVGO')[0], 'percent': change('AVGO')[1]},
            {'name': 'Oracle Corporation', 'symbol': 'ORCL', 'price': price('ORCL'), 'change_price': change('ORCL')[0], 'percent': change('ORCL')[1]}
        ]


        part2 = [
            {'name': 'Eli Lilly and Company', 'symbol': 'LLY', 'price': price('LLY'), 'change_price': change('LLY')[0], 'percent': change('LLY')[1]},
            {'name': 'UnitedHealth Group', 'symbol': 'UNH', 'price': price('UNH'), 'change_price': change('UNH')[0], 'percent': change('UNH')[1]},
            {'name': 'Johnson & Johnson', 'symbol': 'JNJ', 'price': price('JNJ'), 'change_price': change('JNJ')[0], 'percent': change('JNJ')[1]},
            {'name': 'AbbVie Inc.', 'symbol': 'ABBV', 'price': price('ABBV'), 'change_price': change('ABBV')[0], 'percent': change('ABBV')[1]},
            {'name': 'Merck & Co., Inc.', 'symbol': 'MRK', 'price': price('MRK'), 'change_price': change('MRK')[0], 'percent': change('MRK')[1]}
        ]

        part3 = [
            {'name': 'Cheniere Energy, Inc.', 'symbol': 'LNG', 'price': price('LNG'), 'change_price': change('LNG')[0], 'percent': change('LNG')[1]},
            {'name': 'Exxon Mobil Corporation', 'symbol': 'XOM', 'price': price('XOM'), 'change_price': change('XOM')[0], 'percent': change('XOM')[1]},
            {'name': 'Chevron Corporation', 'symbol': 'CVX', 'price': price('CVX'), 'change_price': change('CVX')[0], 'percent': change('CVX')[1]},
            {'name': 'ConocoPhillips', 'symbol': 'COP', 'price': price('COP'), 'change_price': change('COP')[0], 'percent': change('COP')[1]},
            {'name': 'EOG Resources, Inc.', 'symbol': 'EOG', 'price': price('EOG'), 'change_price': change('EOG')[0], 'percent': change('EOG')[1]}
        ]
    elif count == 2:
        part1 = [
            {'name': 'GE Aerospace', 'symbol': 'GE', 'price': price('GE'), 'change_price': change('GE')[0], 'percent': change('GE')[1]},
            {'name': 'Caterpillar Inc.', 'symbol': 'CAT', 'price': price('CAT'), 'change_price': change('CAT')[0], 'percent': change('CAT')[1]},
            {'name': 'RTX Corporation', 'symbol': 'RTX', 'price': price('RTX'), 'change_price': change('RTX')[0], 'percent': change('RTX')[1]},
            {'name': 'Honeywell International', 'symbol': 'HON', 'price': price('HON'), 'change_price': change('HON')[0], 'percent': change('HON')[1]},
            {'name': 'Eaton Corporation', 'symbol': 'ETN', 'price': price('ETN'), 'change_price': change('ETN')[0], 'percent': change('ETN')[1]}
        ]
        part2 = [
            {'name': 'Berkshire Hathaway Inc.', 'symbol': 'BRK-B', 'price': price('BRK-B'), 'change_price': change('BRK-B')[0], 'percent': change('BRK-B')[1]},
            {'name': 'JPMorgan Chase & Co.', 'symbol': 'JPM', 'price': price('JPM'), 'change_price': change('JPM')[0], 'percent': change('JPM')[1]},
            {'name': 'Visa Inc.', 'symbol': 'V', 'price': price('V'), 'change_price': change('V')[0], 'percent': change('V')[1]},
            {'name': 'Mastercard Incorporated', 'symbol': 'MA', 'price': price('MA'), 'change_price': change('MA')[0], 'percent': change('MA')[1]},
            {'name': 'Bank of America', 'symbol': 'BAC', 'price': price('BAC'), 'change_price': change('BAC')[0], 'percent': change('BAC')[1]}
        ]
        part3 = [
            {'name': 'Walmart Inc.', 'symbol': 'WMT', 'price': price('WMT'), 'change_price': change('WMT')[0], 'percent': change('WMT')[1]},
            {'name': 'Costco Wholesale', 'symbol': 'COST', 'price': price('COST'), 'change_price': change('COST')[0], 'percent': change('COST')[1]},
            {'name': 'The Procter & Gamble', 'symbol': 'PG', 'price': price('PG'), 'change_price': change('PG')[0], 'percent': change('PG')[1]},
            {'name': 'The Coca-Cola Company', 'symbol': 'KO', 'price': price('KO'), 'change_price': change('KO')[0], 'percent': change('KO')[1]},
            {'name': 'PepsiCo, Inc.', 'symbol': 'PEP', 'price': price('PEP'), 'change_price': change('PEP')[0], 'percent': change('PEP')[1]}
        ]
    else:
        part1 = [
            {'name': 'Amazon.com, Inc.', 'symbol': 'AMZN', 'price': price('AMZN'), 'change_price': change('AMZN')[0], 'percent': change('AMZN')[1]},
            {'name': 'Tesla, Inc.', 'symbol': 'TSLA', 'price': price('TSLA'), 'change_price': change('TSLA')[0], 'percent': change('TSLA')[1]},
            {'name': 'The Home Depot, Inc.', 'symbol': 'HD', 'price': price('HD'), 'change_price': change('HD')[0], 'percent': change('HD')[1]},
            {'name': "McDonald's Corporation", 'symbol': 'MCD', 'price': price('MCD'), 'change_price': change('MCD')[0], 'percent': change('MCD')[1]},
            {'name': 'Booking Holdings Inc.', 'symbol': 'BKNG', 'price': price('BKNG'), 'change_price': change('BKNG')[0], 'percent': change('BKNG')[1]}
        ]
        part2 = [
            {'name': 'Linde plc', 'symbol': 'LIN', 'price': price('LIN'), 'change_price': change('LIN')[0], 'percent': change('LIN')[1]},
            {'name': 'The Sherwin-Williams', 'symbol': 'SHW', 'price': price('SHW'), 'change_price': change('SHW')[0], 'percent': change('SHW')[1]},
            {'name': 'Southern Copper', 'symbol': 'SCCO', 'price': price('SCCO'), 'change_price': change('SCCO')[0], 'percent': change('SCCO')[1]},
            {'name': 'Nucor Corporation', 'symbol': 'NUE', 'price': price('NUE'), 'change_price': change('NUE')[0], 'percent': change('NUE')[1]},
            {'name': 'Ecolab Inc.', 'symbol': 'ECL', 'price': price('ECL'), 'change_price': change('ECL')[0], 'percent': change('ECL')[1]}
        ]
        part3 = [
            {'name': 'NextEra Energy, Inc.', 'symbol': 'NEE', 'price': price('NEE'), 'change_price': change('NEE')[0], 'percent': change('NEE')[1]},
            {'name': 'The Southern Company', 'symbol': 'SO', 'price': price('SO'), 'change_price': change('SO')[0], 'percent': change('SO')[1]},
            {'name': 'GE Vernova Inc.', 'symbol': 'GEV', 'price': price('GEV'), 'change_price': change('GEV')[0], 'percent': change('GEV')[1]},
            {'name': 'Duke Energy Corporation', 'symbol': 'DUK', 'price': price('DUK'), 'change_price': change('DUK')[0], 'percent': change('DUK')[1]},
            {'name': 'Constellation Energy', 'symbol': 'CEG', 'price': price('CEG'), 'change_price': change('CEG')[0], 'percent': change('CEG')[1]}
        ]
    return render_template("home.html", count=count, part1=part1, part2=part2, part3=part3)

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        session['company'] = request.form.get("comp", session.get('company', '')).upper()

    company = session.get('company', '').upper()
    if not company:
        return apology("Company symbol is missing")

    df = yf.Ticker(company)
    information = df.info
    price = information.get('currentPrice', None)

    if price is not None:
        session['price'] = round(price, 2)

    # Lấy dữ liệu giá lịch sử
    interval = "1m" if time() else "1d"
    hist_price = df.history(period="1d", interval=interval)

    if not hist_price.empty:
        this_price = hist_price['Open'].iloc[0]
        last_price = hist_price['Close'].iloc[-1]

        session['sign'] = last_price > this_price
        session['change_price'], session['percent'] = change(company)

    # Chart dữ liệu
    hist = df.history(period='1d', interval="1m")
    session['line'] = {
        "labels": hist.index.strftime('%Y-%m-%d %H:%M:%S').tolist(),
        "values": hist['Close'].tolist(),
    }
    return render_template("profile.html", info=information)


@app.route("/update-price", methods=["GET"])
def updatePrice():

    df = yf.Ticker(session['company'])
    information = df.info
    price = information['currentPrice']

    if time():
        hist_price = df.history(period="1d", interval="1m")
    else:
        hist_price = df.history(period="1d", interval="1d")

    this_price = hist_price['Open'].iloc[0]
    last_price = hist_price['Close'].iloc[-1]

    sign = False
    if last_price:
        compare = last_price - this_price
        sign = compare > 0

    change_price, percent = change(session['company'])

    return jsonify({
        "price": round(price, 2),
        "sign": sign,
        "change_price": change_price,
        "percent": percent
    })
@app.route("/history", methods=["GET", "POST"])
def history():
    session['ranNum'] = random.randint(0, 9)
    start_input = None
    end_input = None
    session.setdefault('company', "AAPL")
    if 'interval' not in session or not session['interval']:
        session['interval'] = '1d'
    if 'time' not in session or not session['time']:
        session['time'] = '6mo'

    # Lưu vào để khi reload lại thì về giá trị ban đầu
    time = session['time']
    interval = session['interval']

    # Reset Khi Reload Page
    session['time'] = '6mo'
    session['interval'] = '1d'

    if request.method == "POST":
        timeType = request.form.get('timeType')
        if timeType == "time":
            session['time'] = request.form.get('time', session['time'])
            session['interval'] = interval
        if timeType == "interval":
            session['interval'] = request.form.get('interval', session['interval'])
            session['time'] = time
        if timeType == "input":
        # Save time to when apology can return to previous page by using get to get time
            start_input = request.form.get("start_input")
            end_input = request.form.get("end_input")

            if start_input and not validate(start_input):
                return apology("Invalid Start Date", 400)
            elif end_input and not validate(end_input):
                return apology("Invalid End Date", 400)


    df = yf.Ticker(session['company'])
    information = df.info
    if start_input and end_input:
        hist = df.history(start=start_input, end=end_input, interval=session['interval'])
        start_date = start_input
        end_date = end_input
    else:
        hist = df.history(period=session['time'], interval=session['interval'])
        if isinstance(hist.index, pd.DatetimeIndex):
            start_date = hist.index.min().strftime('%Y-%m-%d')
            end_date = hist.index.max().strftime('%Y-%m-%d')
    hist = hist.round(2)

    if isinstance(hist.index, pd.DatetimeIndex):
        hist.index = hist.index.strftime('%Y-%m-%d')

    data = hist.reset_index().to_dict("records")[::-1]
    return render_template("history.html", value=data, info=information, start=start_date, end=end_date)

@app.route("/news", methods=["GET", "POST"])
def news():
    session['ranNum'] = random.randint(0, 9)
    df = yf.Ticker(session['company'])
    info = df.info
    news = df.news
    list = []
    for time in news:
        current = datetime.now()
        current = int(current.timestamp())
        diff = current - time['providerPublishTime']
        hours = diff / 3600
        if hours < 1:
            minutes = diff / 60
            if minutes < 1:
                list.append(f"{diff:.0f} seconds ago")
            else:
                list.append(f"{minutes:.0f} minutes ago")
        else:
            if hours > 24:
                days = diff/86400
                if days == 1:
                    list.append(f"{days:.0f} day ago")
                else:
                    list.append(f"{days:.0f} days ago")
            elif hours == 1:
                list.append(f"{hours:.0f} hour ago")
            else:
                list.append(f"{hours:.0f} hours ago")
    return render_template("news.html", news=news, list=list, info=info)

@app.route("/financial", methods=["GET", "POST"])
def financial():
    df = yf.Ticker(session['company'])
    info = df.info
    financials = "income_stmt"
    if request.method == "POST":
        financials = request.form.get("financials")

    if financials == "income_stmt":
        data = pd.DataFrame(df.financials.fillna("--")).iloc[::-1]
    elif financials == "balance_sheet":
        data = pd.DataFrame(df.balance_sheet.fillna("--")).iloc[::-1]
    else:
        data = pd.DataFrame(df.cashflow.fillna("--")).iloc[::-1]

    financial = data.applymap(lambda x: f"{x:,.0f}" if isinstance(x, (int, float)) else x)
    time = data.columns.strftime("%Y/%m/%d")
    breakdown = data.transpose().columns

    return render_template("financial.html", info=info, financials=financials, financial = financial, time=time, breakdown=breakdown)

@app.route("/analysis", methods=["GET", "POST"])
def analysis():
    session['ranNum'] = random.randint(0, 9)
    try:
        df = yf.Ticker(session['company'])
        information = df.info
        earning = convert(df.earnings_estimate)
        revenue = convert(df.revenue_estimate)
        trend = convert(df.eps_trend)
        revision = convert(df.eps_revisions)
        growth = convert(df.growth_estimates)
    except KeyError as e:
        growth = [{"LTG": "--"}]
    return render_template("analysis.html", earning=earning, revenue=revenue, trend=trend, revision=revision, growth=growth, info=information)
def convert(data):
    if data is None or data.empty:
        return [{"--": "--"}]
    data_df = pd.DataFrame(data)
    data_df = data_df.transpose()
    data_df = data_df.applymap(divide)
    data_records = data_df.to_dict("records")
    return data_records
def divide(value):
    if pd.isna(value):
        value = "--"
        return value
    if isinstance(value, (int, float)):
        if value >= 1e9:
            return f"{round(value / 1e9, 2)}B"
        elif value >= 1e6:
            return f"{round(value / 1e6, 2)}M"
        elif value >= 1e3:
            return f"{round(value / 1e3, 2)}K"
        return round(value, 2)
    return value

@app.route("/chart", methods=["GET", "POST"])
def chart():
    df = yf.Ticker(session['company'])
    info = df.info
    if 'timeChart' not in session:
        session['timeChart'] = '1d'
    if 'optionChart' not in session:
        session['optionChart'] = 'Candle'
    # Lưu vào để khi reload lại thì về giá trị ban đầu
    timeChart = session['timeChart']
    optionChart = session['optionChart']

    # Reset Khi Reload Page
    session['timeChart'] = '1d'
    session['optionChart'] = 'Candle'


    # Handle POST requests
    if request.method == 'POST':
        form_type = request.form.get('formType')
        if form_type == 'timeChart':
            session['timeChart'] = request.form.get('timeChart', session['timeChart'])
            session['optionChart'] = optionChart

        elif form_type == 'chartType':
            session['optionChart'] = request.form.get('optionChart', session['optionChart'])
            session['timeChart'] = timeChart

    isLine = session['optionChart'] != "Candle"

    # Get data over time
    if session['timeChart'] == "1d":
        data = df.history(period="1d", interval="1m")
    elif session['timeChart'] == "max":
        data = df.history(period=session['timeChart'], interval="1mo")
    elif session['timeChart'] == "5y":
        data = df.history(period=session['timeChart'], interval="1wk")
    else:
        data = df.history(period=session['timeChart'], interval="1d")

    # Data For Line Chart
    line = [
        {
            'x': row.name.timestamp() * 1000,
            'y': [round(row['Close'], 2)]
        }
        for _, row in data.iterrows()
    ]

    # Data For CandleStick Chart
    candlestick = [
        {
            'x': row.name.timestamp() * 1000,
            'y': [round(row['Open'], 2), round(row['High'], 2), round(row['Low'], 2), round(row['Close'], 2)]
        }
        for _, row in data.iterrows()
    ]

    return render_template('chart.html', isLine=isLine, candlestick=candlestick, info=info, line=line)

if __name__ == "__main__":
    app.run(debug=True)
