```markdown
# WhatsApp Automated Image and Message Sender

This Python script utilizes Selenium WebDriver to automate the process of sending images and messages through WhatsApp web. It reads phone numbers from a file, sends an image along with a predefined message to each recipient.

## Prerequisites

- Python installed on your machine.
- Selenium WebDriver and Chrome WebDriver installed (`pip install selenium webdriver_manager`).
- Chrome browser installed.

## Setup

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Place your image file (`image.png`) and message text file (`message.txt`) in the project directory.
4. Update the `numbers.txt` file with the list of recipient phone numbers (one per line).
5. Adjust configuration parameters in the script if necessary.

## Configuration Parameters

- `login_time`: Time for login (in seconds).
- `new_msg_time`: Time for a new message (in seconds).
- `send_msg_time`: Time for sending a message (in seconds).
- `country_code`: Set your country code.
- `action_time`: Set time for button click action.
- `image_path`: Absolute path to your image.

## Usage

1. Run the script using `python whatsapp_automation.py`.
2. Scan the QR code displayed on the browser window to log in to WhatsApp web.
3. The script will iterate through the phone numbers, sending the image and message to each recipient.

## Troubleshooting

- If you encounter any issues, check the error messages printed in the console.
- Ensure that all files and directories are correctly set up as described in the setup section.
- Verify that Chrome WebDriver is compatible with your Chrome browser version.

## Example

```bash
python whatsapp_automation.py
```

## Note

- This script is for educational purposes only. Use it responsibly and avoid violating WhatsApp's terms of service.

```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
