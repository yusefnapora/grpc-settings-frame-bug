name := "grpc-http2-bug-server"

version := "1.0"

scalaVersion := "2.11.8"

import com.trueaccord.scalapb.{ScalaPbPlugin => PB}

PB.protobufSettings

PB.runProtoc in PB.protobufConfig := (args =>
  com.github.os72.protocjar.Protoc.runProtoc("-v300" +: args.toArray))

version in PB.protobufConfig := "3.0.0-beta-2"

libraryDependencies ++= Seq(
  "io.grpc" % "grpc-netty" % "0.14.0",
  "com.trueaccord.scalapb" %% "scalapb-runtime-grpc" % (PB.scalapbVersion in PB.protobufConfig).value
)