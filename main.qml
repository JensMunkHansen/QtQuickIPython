import QtQuick 2.15
import QtQuick.Window 2.15
import QmlInterpreter 1.0

Rectangle {
    width: 640
    height: 480
    visible: true
    //title: qsTr("Hello World")
    color: "black"

    InterpreterItem {
        focus: true
        fillColor: "#000000"
        id: interpreter
        anchors.fill: parent
        Component.onCompleted: {
            initInterpreter()
        }
    }
}
