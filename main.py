from dotenv import load_dotenv
from crew import stock_crew

load_dotenv()

def run(stock: str, risk_tolerance: str = "Medium", investment_horizon: str = "Medium-term"):
    result = stock_crew.kickoff(inputs={
        "stock": stock,
        "risk_tolerance": risk_tolerance,
        "investment_horizon": investment_horizon
    })
    print(result)

if __name__ == "__main__":
    run("BMW")
