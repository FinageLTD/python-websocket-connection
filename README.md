### Connect to Finage Market Source via WebSocket

Install the required library to create a WebSocket connection.
`pip install websockets`

### Usage

Replace the server URL in the script with your server address [line 5];
`uri = "YOUR_SERVER_ADDRESS"`

Run the script:
`python3 websocket.py`

After running the script, it will ask you to enter a symbol name
`Enter the currency symbol: BTCUSD`

We've entered the _BTCUSD_ in this example.


### Output
Example output after running the Python script.
```javascript
< {"Message":"Authorizing..."}
< {"status_code":200,"message":"Connected to the Cryptocurrency Market source."}
< {"s":"BTCUSD","p":"31538.52000000","q":"0.00527200","t":1626875142626}
< {"s":"BTCUSD","p":"31538.52000000","q":"0.00653000","t":1626875142626}
```

> You can enter your _US Market_, _Canada Market_, _Forex_, _Cryptocurrency_, _Index_, _ETF_, etc. market server address to use this script. [Check out the Finage](https://finage.co.uk) for all products.

Real-Time stream is ready to use just in three steps.
[Connect to your own WebSocket server](https://finage.co.uk/#pricing)
[Get consultation](https://finage.co.uk/consultation)