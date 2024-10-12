from dotenv import load_dotenv
from dash import Dash, html

def main():
    load_dotenv()
    app = Dash()
    app.layout = [html.Div(children='Hello World')]

    app.run(debug=True)

if __name__ == '__main__':
    main()