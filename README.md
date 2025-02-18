# Countdown for Email Marketing
Hi, this is a template to create email marketing campaigns with a countdown banner.

## Why use it?
One strong wey to increase your convertions is using the feeling of urgency. But with the strict rules imposed by providers for email marketing, it could be hard to transmit it visualy.
This is a great solution for this issue by having a way to amplify use feeling.

## How it works
Global steps that could be helpfull:
Based on the desired date, and the now date, it generates a sequence of images/gif in countdown.
Each frame has 1 second span time visible and switches to another one.

This is all the steps to use it properly, but consider the backend steps are'nt coded.
1. [Frontend] The data to create the banner should be sent to the _backend_. 
2. [Backend] Generate a route where the requests will come, based on the fontend given data.
3. [Backend] Run the code to create the gif, on requests come.
4. [Backend] Send the gif as response to the request.
5. [Marketing] Use the route path in the _src_ attribute in the _img_ tag.

## What is coded
- Countdown form now date to desired date
- Custom font family and size
- Custom font and background colors
- Custom background image (if it can't get the image, it uses the setted up color)
- Custom number position (You need to define the box position for each number, it can be easier if used a frontend to adjust it)
- Gif creation

## Future updates
- Generate a fully working frontend to be easier to configure the gif
- Generate a better structure and refine the code
- Turn the code fully english
