# Discord Webhook Script

## Dependencies

Python 3: [Download link](https://www.python.org/downloads/)

Python `requests` module: To install, enter the following command in cmd or a terminal:

```
pip install requests
```

## Usage

1. Create a file named `list.txt` in the same directory as `,/discord_webhook_script/check_shopify_stock_webhook.py`. The file should contain a newline separated list of urls for items to check stock of. 

    For example: 
    ```
    https://examplestore.com/products/exampleproduct
    https://examplestore.com/products/exampleproduct2?variant=39615971195628
    https://examplestore.com/collections/examplecollection/products/exampleproduct3
    ```

    To check only specific variants of a product, be sure to use a url with the correct `?variant={variantid}` suffix. 
    
    To check all variants of a product, remove the `?variant={variantid}` suffix from the url if it appears.

2. Run `./discord_webhook_script/check_shopify_stock_webhook.py` then close it to generate default settings file.

3. Open `config.cfg` and add your discord webhook url for `url = `.

4. Edit `content = ` to configure the message content you want to send when a product goes from out of stock to in stock.

    `{Name}` sends the item's name.

    `{Title}` sends the item's title.

    `{SKU}` sends the item's sku.

    `{Public Title}` sends the item's public title.

    `{Option1}` sends the item's option1.

    `{Option2}` sends the item's option2.

    `{Option3}` sends the item's option3.

    `{Link}` sends a link to the item's store page.

5. Optionally, edit the delays in `config.cfg` to change the delay in seconds between checking stock, looping batch, and request fail.

    `stock_delay` adds a delay after sending the stock check request.

    `batch_delay` adds a delay between checking the full list of products. Only used between the last item in the list and the first item in the list when looping back to the first item.

    `request_fail_delay` adds a delay after a request fails before resuming the sending of requests.

6. Run `./discord_webhook_script/check_shopify_stock_webhook.py`

## Troubleshooting

To reset settings to default, delete `config.cfg` and run the script. A new `config.cfg` will be generated with defaults.

To reset stock states and tracking, delete `stock_state.json`. This will remove the current stock data collected by the script. Upon running the script again it will rerecord the stock states. This will cause the script to resend webhook messages for items that had previously been recorded as in stock and have not had a change in state.