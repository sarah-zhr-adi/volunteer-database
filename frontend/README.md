## Forcing a Code Style

There is a pre-commit hook that will run [ESLint](https://eslint.org/) and [Prettier](https://prettier.io/) in "autofix"
mode on all of the staged files. If either fails, the commit will be aborted
and you'll have to manually fix the problems. You can use the following scripts
to help identifying/fixing the problems before a commit:

### `yarn lint`

Will lint all of the `.js` and `.jsx` files inside the `/src` folder.

### `yarn prettify`

Will format all of the code inside the `/src` folder. If you want to change a rule or set a certain style, talk to the leads first so if there is a major change it's being communicated properly.

## Linting/Formatting Plugins

In addition to the scripts, you can install ESLint and Prettier plugins for your
editor/IDE:

### VSCode
[VSCode ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)<br />
[VSCode Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)<br /><br />
Add the following in the (workspace) `settings.json` to point VSCode ESLint to the right directory:
```json
{
  "eslint.workingDirectories": ["./frontend"]
}
```
Optionally add also the following to enable code lint/format on save:
```json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
      "source.fixAll.eslint": true
  },
  "[javascript]": {
      "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[html]": {
      "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[jsonc]": {
      "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
``` 
<br />
<br />


This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available CRA Scripts

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.<br />
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br />
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `yarn eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: https://facebook.github.io/create-react-app/docs/code-splitting

### Analyzing the Bundle Size

This section has moved here: https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size

### Making a Progressive Web App

This section has moved here: https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app

### Advanced Configuration

This section has moved here: https://facebook.github.io/create-react-app/docs/advanced-configuration

### Deployment

This section has moved here: https://facebook.github.io/create-react-app/docs/deployment

### `yarn build` fails to minify

This section has moved here: https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify
