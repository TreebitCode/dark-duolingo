# Dark mode for Duolingo web
This is a dark mode for Duolingo's website that tries to replicate the dark mode of the mobile app version of Duolingo as closely as possible using CSS. This is still a work in progress. Please see the [Issues tab](https://github.com/TreebitCode/dark-duolingo/issues) for more info.

## Instructions
To use the dark mode, please download the file called `dark-duolingo.css` and apply it to Duolingo's website using a browser extension for applying custom CSS.

## Implementation
The colors of every element are changed to the ones used in the mobile version, unless the element is already consistent between the two versions. The colors are retrieved from the app using a color picking application and stored in CSS variables for readability. Some rarely used colors are not saved in variables, because variables for them already exist in the official Duolingo CSS. In this case, the official variables are reused.

Some elements only exist in the web version, in which case an element is found that is as close in function and appearance to the web-only element as possible. That element's colors are then used for the web-only element. Alternatively, an element with identical colors in the light mode version of the website is found, and its colors are used for the web-only element.

To avoid using custom images, the colors of most SVG icons are changed using the `filter` property. The filters are created using [this tool](https://codepen.io/sosuke/pen/Pjoqqpthis) and saved as CSS variables for readability. This approach is tedious, since the generated filter's precision is based on random chance, so getting a filter that returns the exact color can take many attempts.

When an icon cannot be recolored with filters, a custom image is created and uploaded to the [Images folder](https://github.com/TreebitCode/dark-duolingo/tree/main/images).

Some element behaviors cannot be ported using only CSS. In which case, they are replicated as closely as possible within the constraints.

Some elements' `opacity` and/or `brightness` properties on hover are altered to create a level of contrast that is more consistent with the light mode version.
