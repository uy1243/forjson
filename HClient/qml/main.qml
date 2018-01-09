import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Window 2.2
import "." as App

Rectangle {
	id:mainlogin
	width:300
	height:300
	
	property var testa:"123"
           MouseArea{
                id: mouseArea

                anchors.fill: parent
               onClicked: {console.log("ji!")
 				mainlogin.testa="qwe"}
                   }
                   onTestaChanged:{
               	
               console.log("changge!")
               }
                }
                
               
