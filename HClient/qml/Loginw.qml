import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2
import QtQml 2.0 as QML



ApplicationWindow {
    visible: true
    width: 240
    height: 240
    title: qsTr("旅鸽")
    color: "whitesmoke"
	id:loginw
	
	

    GridLayout {
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.margins: 9
        columns: 2
        rows: 4
        rowSpacing: 10
        columnSpacing: 10

        Text {
            text: qsTr("用户名：")
        }

        // Input field of the first number
        TextField {
            id: username
        }

        Text {
            text: qsTr("密码：")
        }

        // Input field of the second number
        TextField {
            id: passw
        }

        Button {
            height: 40
            Layout.fillWidth: true
            text: qsTr("登录")

            Layout.columnSpan: 1

            onClicked: {
                // Invoke the calculator slot to sum the numbers
                loginCh.flogin(username.text, passw.text)
            }
        }
        Button {
        	id: ca
            height: 40
            Layout.fillWidth: true
            text: qsTr("取消")

            Layout.columnSpan: 1

            onClicked: {
                // Invoke the calculator slot to subtract the numbers
               

     var component = Qt.createComponent("Mainw.qml")
                        if (component.status ==Component.Ready) {
                        console.log("in b")
                        var dialog = component.createObject(loginw)
                        dialog.sqlPosition = positionRoot
                        dialog.show();
                        }
               loginCh.fcancel()
            }
        }
}
    Connections {
        target:loginCh

      onLogin:
      {
      	if (te1==1)
 
      		console.log("p")
      }
    }


 }
