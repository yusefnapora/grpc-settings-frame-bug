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

You should see output similar to

```
saying hello...
response: Hello world
saying hello...
response: Hello world
saying hello...
response: Hello world
saying hello...
failed after 3 attempts with error: NetworkError(code=StatusCode.UNAVAILABLE, details="")
```

on the client, and on the server:

```
Jun 16, 2016 6:09:44 PM io.grpc.netty.NettyServerTransport notifyTerminated
SEVERE: Transport failed
io.netty.handler.codec.http2.Http2Exception: First received frame was not SETTINGS. Hex dump for first 5 bytes: 0000040800
	at io.netty.handler.codec.http2.Http2Exception.connectionError(Http2Exception.java:82)
	at io.netty.handler.codec.http2.Http2ConnectionHandler$PrefaceDecoder.verifyFirstFrameIsSettings(Http2ConnectionHandler.java:300)
	at io.netty.handler.codec.http2.Http2ConnectionHandler$PrefaceDecoder.decode(Http2ConnectionHandler.java:209)
	at io.netty.handler.codec.http2.Http2ConnectionHandler.decode(Http2ConnectionHandler.java:391)
	at io.netty.handler.codec.ByteToMessageDecoder.callDecode(ByteToMessageDecoder.java:387)
	at io.netty.handler.codec.ByteToMessageDecoder.channelRead(ByteToMessageDecoder.java:245)
	at io.netty.channel.ChannelHandlerInvokerUtil.invokeChannelReadNow(ChannelHandlerInvokerUtil.java:83)
	at io.netty.channel.DefaultChannelHandlerInvoker.invokeChannelRead(DefaultChannelHandlerInvoker.java:154)
	at io.netty.channel.AbstractChannelHandlerContext.invokeChannelRead(AbstractChannelHandlerContext.java:354)
	at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:145)
	at io.netty.channel.DefaultChannelPipeline.fireChannelRead(DefaultChannelPipeline.java:1078)
	at io.netty.channel.nio.AbstractNioByteChannel$NioByteUnsafe.read(AbstractNioByteChannel.java:117)
	at io.netty.channel.nio.NioEventLoop.processSelectedKey(NioEventLoop.java:527)
	at io.netty.channel.nio.NioEventLoop.processSelectedKeysOptimized(NioEventLoop.java:484)
	at io.netty.channel.nio.NioEventLoop.processSelectedKeys(NioEventLoop.java:398)
	at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:370)
	at io.netty.util.concurrent.SingleThreadEventExecutor$5.run(SingleThreadEventExecutor.java:742)
	at io.netty.util.concurrent.DefaultThreadFactory$DefaultRunnableDecorator.run(DefaultThreadFactory.java:145)
	at java.lang.Thread.run(Thread.java:745)
	```
	
