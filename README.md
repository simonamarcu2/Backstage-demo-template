# Backstage-demo-template

Backstage PoC learning and development

## Create your Backstage App

To install the Backstage Standalone app, we make use of npx, a tool to run Node executables straight from the registry. This tool is part of your Node.js installation. Running the command below will install Backstage. The wizard will create a subdirectory inside your current working directory.

```sh
npx @backstage/create-app
```

## Add external plugin 

- ! Note: Integrations may already be set up as part of your app-config.yaml.

This is done in your app-config.yaml by adding Backstage integrations for the appropriate source code repository for your organization.


- You can configure the author and commit message through the scaffolder configuration in app-config.yaml:

scaffolder:
  defaultAuthor:
    name: Example Name # Defaults to `Scaffolder`
    email: example@email.com # Defaults to `scaffolder@backstage.io`
  defaultCommitMessage: "My first commit" # Defaults to 'Initial commit'

- To configure who can see the new repositories created from software templates, add the repoVisibility key within a software template:

  id: publish
  name: Publish
  action: publish:github
  input:
    repoUrl: '{{ parameters.repoUrl }}'
    repoVisibility: public # or 'internal' or 'private'

## Add template

## To start the app, run

```sh
yarn install
yarn dev
```





*nunjacks*
*<http://httpbin.org/#/>*
*curl -X GET "https://httpbin.org/get" -H "accept: application/json"*


# React Scaffolding

Tired of duplicating that old base component for creating a new one? React Scaffolding helps you to Scaffold various types of React Components quickly

Just run

```bash
npx react-scaffolding --name=yourComponentName --template=[function|class|pure]
```

Or

### Install
```
npm install -g react-scaffolding
```

With React Scaffolding you can create the following types of React Components:

- Function
- Class extending PureComponent
- Class extending Component

### Example
```bash
$ react-scaffolding --name=my-component --path=my-folder --template=function --css my-stylesheet
```

Will create the following files on the directory **my-folder** using the **function** template:

*my-component.js*
```jsx harmony
import React from 'react';
import './mycomponent.css';

const MyComponent = (props) => (
  <div></div>
);

export default MyComponent;
```

*my-stylesheet.css*

```css
.my-component { }
```

### More examples
The following command will generate a file named **MyContainer** on the directory **path_to_my_folder** using the default **class** template
```bash
> react-scaffolding --name=MyContainer --path=path_to_my_folder
```
The following command will generate a file named **MyWrapper** on the directory **path to my folder** using the template **wrapper**
```bash
> react-scaffolding --name=MyWrapper --path="path to my folder" --template=wrapper
```
The following command will generate a file named **CustomContainer** on the directory **pathToMyFolder** using the template **customTemplate** that is located on the directory **path_to_scaffold_templates**  
- Please NOTE that you **MUST** ensure that the target directories already exist and you have read and write permissions to them!
```bash
> react-scaffolding --name=CustomContainer --path=pathToMyFolder --template=customTemplate --templatePath path_to_scaffold_templates
```

### Options

```text
  --help            Ignores all other options and shows this message

  --path            The directory where the component will be placed

  --template        The template that will be used to create your component
                    Those are the available templates:
                    - class     (default)
                    - pure
                    - function
                    - wrapper
                    - container (intended to work with row)
                    - row       (intended to work with container)

  --templatePath    The directory where to read the templates files from

  --css             Allows the creation of a default css file and imports it on the component.
                    - If no filename is passed, then the same name as the --name option will be used.
                    - If a file name is passed, then creates the default css file with the given name.
```

### Making changes and testing
1. Clone the repository `git clone https://github.com/gabrielbs/react-scaffolding.git`
2. Install the dependencies `npm install`
3. Implement your changes
4. Create a link on your machine to your repository changes `npm link`
5. Create a new directory where you will test the changes or go to the project directory where you want to use the tool
6. Import the linked repository `npm link react-scaffolding`
7. Use the module via it's command `react-scaffolding --help`

## License
[MIT](http://opensource.org/licenses/MIT) ©
