# grpc-settings-frame-bug


This repo has a minimal grpc service that exhibits a connection issue when run on an ubuntu (and possibly other linux) environment.

### setup
If you use [vagrant](https://vagrantup.com), the Vagrantfile in this repo should set up a box with the necessary dependencies,
otherwise you'll need to [install sbt](http://www.scala-sbt.org/0.13/docs/Setup.html), and the following apt packages
(assuming a debian / ubuntu environment):

- python-dev
- python-pip
- python-virtualenv
- libtool
- autoconf
- automake

and it's also a good idea to upgrade pip from the system-installed version with `sudo pip install --upgrade pip`


### running
The service can be run with sbt by changing to the `grpc-http2-bug-server` directory (in vagrant this will be mounted at `/vagrant/grpc-http2-bug-server`)
and running `sbt 'run-main org.napora.HelloWorldServer'`

Once that's running, go to the `grpc-http2-bug-client` directory in a new shell, and install the python dependencies in a new virtualenv:

```bash
virtualenv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

then run the client with `python -m helloclient.main localhost 50051`

