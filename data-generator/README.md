# Data generator
You can generate fake data based upon the data dictionaries included.

## Prerequisites
You need the following tools to use the data-generator:

- [npm](https://nodejs.org/en/)
- [fakeit](https://github.com/bentonam/fakeit)
  - [FakerJS](http://marak.github.io/faker.js/)
  - [ChanceJS](https://chancejs.com/)
- [git](https://git-scm.com/downloads)

### Installation
Install NPM first on your system.

**Mac**

Download it from [npm](https://nodejs.org/en/). Install the package by clicking on it.

When you have installed NodeJS you can run the following command on the commandline in the terminal:

```bash
npm install fakeit -g
```

There you are all set to use ```fakeit```.


If do not have ```git``` on your system, download it here: [git](https://git-scm.com/downloads). Execute the installer.

Then on the commandline you can execute this:

```batch
git clone https://github.com/lifecycle-project/data.git
```

Now you are all set to generate fake data.

**Windows**

Download it from [npm](https://nodejs.org/en/). Install the package by clicking on it.

When you have installed NodeJS you can run the following command on the commandline in the terminal:

```batch
npm install fakeit -g
```

There you are all set to use ```fakeit```.

You will have to clone this repository to obtain the models for generating fake data.

If do not have ```git``` on your system, download it here: [git](https://git-scm.com/downloads). Execute the installer.

Then on the commandline you can execute this:

```batch
git clone https://github.com/lifecycle-project/data.git
```

Now you are all set to generate fake data.

## Usage

Generate the fake data based upon the dictionaries that are in the ```dictionaries``` directory.

**Mac**

Open a terminal and navigate to the lifecycle-project/data repository:

```bash
cd ~/lifecycle/data; 

fakeit directory output --verbose --count 3000 --format csv dictionaries/
```
You can check the help by executing this command:

```bash
fakeit -h
```

The files will be generated in the output directory. 

**Windows**
Open a commandline interface (execute ```cmd``` on run and execute the following command:

Navigate to the ```lifecycle-project/data``` repository:

```bash
cd ~/lifecycle/data; 

fakeit directory output --verbose --count 3000 --format csv dictionaries/
```

You can check the help by executing this command:

```batch
fakeit -h
```

The files will be generated in the output directory. 

