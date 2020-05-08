# Data generator
You can generate fake data based upon the data dictionaries included.

## Prerequisites
You need the following tools to use the data-generator:

- [npm](https://nodejs.org/en/) *version above 12.16.3*
- [fakeit](https://github.com/bentonam/fakeit)
  - [FakerJS](http://marak.github.io/faker.js/)
  - [ChanceJS](https://chancejs.com/)
- [git](https://git-scm.com/downloads)

### Installation
The installation of the different packages is more or less the same over different platforms. We still have documentation for [Mac](#Mac-installation) and [Windows](#Windows-installation)

#### Mac - installation

Download it from [npm](https://nodejs.org/en/). Install the package by clicking on it. If you already installed NodeJS on your system you can switch version (if needed) by using NVM. Please check: https://nvm.sh.

When you have installed NodeJS you can run the following command on the commandline in the terminal:

```bash
npm install fakeit -g
```

There you are all set to use ```fakeit```.


If you do not have ```git``` on your system, download it here: [git](https://git-scm.com/downloads). Execute the installer.

Then on the commandline you can execute this:

```batch
git clone https://github.com/lifecycle-project/analysis-tools.git
```

Now you are all set to generate fake data.

#### Windows - installation

Download it from [npm](https://nodejs.org/en/). Install the package by clicking on it. If you already installed NodeJS on your system you can switch version (if needed) by using NVM. Please check: https://nvm.sh.

When you have installed NodeJS you can run the following command on the commandline in the terminal:

```batch
npm install fakeit -g
```

There you are all set to use ```fakeit```.

You will have to clone this repository to obtain the models for generating fake data.

If you do not have ```git``` on your system, download it here: [git](https://git-scm.com/downloads). Execute the installer.

Then on the commandline you can execute this:

```batch
git clone https://github.com/lifecycle-project/analysis-tools.git
```

Now you are all set to generate fake data.

## Usage

Generate the fake data based upon the dictionaries that are in the ```dictionaries``` directory. There is currently 1 version of the dictionary: **v1_0**.

### Mac
Open a terminal and navigate to the `~/lifecycle-project/analysis-tools/` repository:

```bash
cd ~/lifecycle/analysis-tools/data-generator; 

fakeit directory output --verbose --count 3000 --format csv dictionaries/

```
You can check the help by executing this command:

```bash
fakeit -h
```

The files will be generated in the output directory. 

### Windows
Open a commandline interface (execute ```cmd```.

Navigate to the `~/lifecycle-project/analysis-tools` repository:

```batch
cd ~/lifecycle/analysis-tools/data-generator; 

fakeit directory output --verbose --count 3000 --format csv dictionaries/
```

You can check the help by executing this command:

```batch
fakeit -h
```

The files will be generated in the output directory. 

