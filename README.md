# Countdown for Email Marketing
This template helps you create email marketing campaigns with a dynamic countdown banner.

## Why use it?
One strong wey to increase your convertions is using the feeling of urgency. But with the strict rules imposed by providers for email marketing, it could be hard to transmit it visualy.
This is a great solution for this issue by having a way to amplify use feeling.

## How it works
Follow these global steps to set up the countdown:
1. Based on the desired end date and the current date, it generates a sequence of images or GIFs for the countdown.
2. Each frame is displayed for 1 second before switching to the next.

Here’s a high-level overview of how to use it:
*Note:* The backend setup isn’t coded yet.

1. **[Frontend]** Send the data required to create the banner to the backend.
2. **[Backend]** Generate a route where requests will be received based on the frontend data.
3. **[Backend]** Run the code to create the GIF whenever a request is received.
4. **[Backend]** Send the GIF back as a response to the request.
5. **[Marketing]** Use the generated route in the _src_ attribute of the _img_ tag in your email.


## What is coded
- Countdown timer from the current date to the desired date
- Customizable font family and size
- Customizable font and background colors
- Option to use a custom background image (if the image can’t be retrieved, it defaults to the set background color)
- Customizable number positioning (you’ll need to define the box position for each number; using a frontend interface for easy adjustments is recommended)
- GIF generation

## Future updates
- A fully functional frontend to simplify GIF configuration
- Improved code structure and optimization
- Full code translation to English
