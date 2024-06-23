# gpt_to_speech_bot

A Telegram bot that integrates with @msspeechbot to convert text responses from a GPT bot into speech and sends the audio back to the original chat. Can be linked with the vk_comments and tg_comments repositories to vocalize GPT responses in the same chat.

## Introduction

The `gpt_to_speech_bot` script is designed to enhance the interaction with GPT bots by converting their text responses into speech. It forwards the text responses from a GPT bot to the @msspeechbot, which converts the text into audio. The audio file is then sent back to the original chat, allowing users to hear the responses.

## Features

- **Forwards Text Messages:** Forwards text responses from a GPT bot to @msspeechbot.
- **Converts Text to Speech:** Uses @msspeechbot to convert text into audio.
- **Sends Back Audio:** Sends the audio file back to the original chat.

## How It Works

1. **Forwarding Text Messages:**  
   The bot forwards any text response containing "GPT4" from the GPT bot to @msspeechbot.

2. **Converting Text to Speech:**  
   @msspeechbot converts the forwarded text into an audio file.

3. **Sending Back Audio:**  
   The bot sends the audio file back to the original chat.

## Getting Started

### Prerequisites

To use this script, you need to have the following:

- Python 3.8 or higher
- A Telegram account
- API credentials from Telegram (API ID and API Hash)

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Commonlist/gpt_to_speech_bot.git
    ```

2. **Install the Required Packages:**  
   Navigate to the project directory and install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up API Credentials:**  
   You need to set up your API credentials for Telegram. You can find the instructions for obtaining these credentials in the respective documentation of Telegram.

### Configuration

Update the script `gpt_to_speech_bot.py` with your API credentials:

    ```python
    api_id = "your_api_id"
    api_hash = "your_api_hash"
    gpt_bot = "Your_GPT_Bot"  # Username of your GPT bot
    ms_speech_bot = "msspeechbot"  # Username of the speech conversion bot
    ```

### Running the Script

To start the script, simply run:

    ```bash
    python gpt_to_speech_bot.py
    ```

or

    ```bash
    nohup python gpt_to_speech_bot.py &
    ```

The script will start monitoring for text responses from the GPT bot.

## Example Usage

- **Step 1:** Send a message to the GPT bot that generates a response containing "GPT4".
- **Step 2:** The bot forwards the text response to @msspeechbot.
- **Step 3:** @msspeechbot converts the text to an audio file.
- **Step 4:** The bot sends the audio file back to the original chat.

## Integration with Other Repositories

This bot can be linked with the following repositories to vocalize GPT responses in the same chat:

- [vk_comments](https://github.com/Commonlist/vk_comments)
- [tg_comments](https://github.com/Commonlist/tg_comments)

## Troubleshooting

If you encounter any issues while using the script, here are some common troubleshooting steps:

- **Check API Credentials:** Ensure that your API ID and API Hash are correct.
- **Internet Connection:** Make sure your internet connection is stable.
- **Script Errors:** If there are any errors in the script, refer to the error message for more details and fix the mentioned issues.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

By using this script, you can convert GPT text responses into speech and enhance the interaction experience.
