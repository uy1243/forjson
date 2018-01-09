import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Layouts 1.1

ApplicationWindow {
    visible: true
    width: 240
    height: 240
    color: "red"
    title:"主界面"
//modality: Qt.ApplicationModal

 
    	ToolBar {
    anchors.fill: parent
    width: 300

//
    RowLayout {
        ToolButton {
            text: qsTr("设置")
            onClicked: {
               user.getId()
                loginCh.fcancel();
            }
        }
        ToolButton {
            text: qsTr("添加")
            onClicked: {

            }
        }
      
    }

TabView {
        id: myContent
        anchors.fill: parent
        
      Item {
    Image {
        source: "../images/zfb.jpg"
    }
    Image {
        x: 80
        width: 100
        height: 100
        source: "../images/zfb.jpg"
    }

     Rectangle { width: 80; height: 80; border.width: 1 }
    Rectangle { x: 20; y: 20; width: 80; height: 80; border.width: 1 }
}
    }
    
    Connections {
        target: loginCh

    }
}
}