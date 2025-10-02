import yfinance as yf
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

MODEL = LiteLlm(model="openai/gpt-4o")


def get_income_statement(ticker: str):
    """
    Retrieves the income statement for comprehensive revenue and profitability analysis.

    This tool fetches detailed income statement data showing a company's financial
    performance over recent reporting periods, including revenues, expenses, and
    profit margins at various levels.

    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL' for Apple Inc.)

    Returns:
        dict: A dictionary containing:
            - ticker (str): The input ticker symbol
            - success (bool): True if the operation was successful
            - income_statement (str): JSON-formatted income statement data including:
                * Total Revenue
                * Cost of Revenue
                * Gross Profit
                * Operating Expenses
                * Operating Income
                * EBITDA
                * Net Income
                * Earnings Per Share (EPS)

    Notes:
        - Data typically covers the last 4 quarters and annual periods
        - All financial figures are in the company's reporting currency
        - Useful for analyzing revenue growth, margin trends, and profitability

    Example:
        >>> get_income_statement('GOOGL')
        {
            'ticker': 'GOOGL',
            'success': True,
            'income_statement': '{"Total Revenue": {...}, "Net Income": {...}}'
        }
    """
    stock = yf.Ticker(ticker)
    # return stock.income_stmt.to_json()
    return {
        "ticker": ticker,
        "success": True,
        "income_statement": stock.income_stmt.to_json(),
    }


def get_balance_sheet(ticker: str):
    """
    Retrieves the balance sheet for analyzing financial position and capital structure.

    This tool fetches comprehensive balance sheet data showing a company's assets,
    liabilities, and shareholders' equity at specific points in time, providing
    insight into financial health and capital efficiency.

    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL' for Apple Inc.)

    Returns:
        dict: A dictionary containing:
            - ticker (str): The input ticker symbol
            - success (bool): True if the operation was successful
            - balance_sheet (str): JSON-formatted balance sheet data including:
                * Current Assets (cash, receivables, inventory)
                * Non-Current Assets (PP&E, intangibles, investments)
                * Current Liabilities (payables, short-term debt)
                * Non-Current Liabilities (long-term debt, deferred items)
                * Total Shareholders' Equity
                * Working Capital components

    Notes:
        - Provides snapshot of financial position at quarter/year end
        - Essential for calculating liquidity ratios (current ratio, quick ratio)
        - Used to assess debt levels, asset efficiency, and book value
        - All values in company's reporting currency

    Example:
        >>> get_balance_sheet('AMZN')
        {
            'ticker': 'AMZN',
            'success': True,
            'balance_sheet': '{"Total Assets": {...}, "Total Liabilities": {...}}'
        }
    """
    stock = yf.Ticker(ticker)
    # return stock.balance_sheet.to_json()
    return {
        "ticker": ticker,
        "success": True,
        "balance_sheet": stock.balance_sheet.to_json(),
    }


def get_cash_flow(ticker: str):
    """
    Retrieves the cash flow statement for analyzing cash generation and capital allocation.

    This tool fetches detailed cash flow data showing how a company generates and
    uses cash across operating, investing, and financing activities, crucial for
    assessing financial sustainability and growth capacity.

    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL' for Apple Inc.)

    Returns:
        dict: A dictionary containing:
            - ticker (str): The input ticker symbol
            - success (bool): True if the operation was successful
            - cash_flow (str): JSON-formatted cash flow statement including:
                * Operating Cash Flow (cash from core business)
                * Capital Expenditures (CapEx)
                * Free Cash Flow (Operating CF - CapEx)
                * Investing Activities (acquisitions, investments)
                * Financing Activities (debt, dividends, buybacks)
                * Net Change in Cash

    Notes:
        - Operating cash flow indicates core business cash generation
        - Free cash flow shows cash available for shareholders/growth
        - Negative investing CF often indicates growth investment
        - Financing CF reveals capital structure decisions
        - Critical for assessing dividend sustainability and growth funding

    Example:
        >>> get_cash_flow('META')
        {
            'ticker': 'META',
            'success': True,
            'cash_flow': '{"Operating Cash Flow": {...}, "Free Cash Flow": {...}}'
        }
    """
    stock = yf.Ticker(ticker)
    # return stock.balance_sheet.to_json()
    return {
        "ticker": ticker,
        "success": True,
        "cash_flow": stock.cash_flow.to_json(),
    }


financial_analyst = Agent(
    name="FinancialAnalyst",
    model=MODEL,
    description="Analyzes detailed financial statements including income, balance sheet, and cash flow",
    instruction="""
    당신은 재무제표 심층 분석을 수행하는 재무 분석가입니다. 업무:

    1. **손익 분석**: get_income_statement()를 사용하여 매출, 수익성, 마진 분석
    2. **재무상태표 분석**: get_balance_sheet()를 사용하여 자산, 부채, 재무 상태 검토
    3. **현금흐름 분석**: get_cash_flow()를 사용하여 현금 창출과 자본 배분 평가

    **사용 가능한 재무 도구:**
    - **get_income_statement(ticker)**: 매출, 이익률, 수익성 분석
    - **get_balance_sheet(ticker)**: 자산, 부채, 자본, 재무 건전성 비율
    - **get_cash_flow(ticker)**: 영업현금흐름, 잉여현금흐름, 자본지출

    포괄적인 재무제표 데이터를 사용하여 기업의 재무 건전성과 성과를 분석하세요.
    기업의 재무 강점을 나타내는 핵심 재무 비율, 추세, 지표에 집중하세요.
    """,
    tools=[
        get_income_statement,
        get_balance_sheet,
        get_cash_flow,
    ],
    output_key="financial_analyst_result",
)
