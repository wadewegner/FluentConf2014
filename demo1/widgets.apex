@RestResource(urlMapping='/Widgets/*')
global class WidgetController {

    @HttpGet
    global static List<Widget__c> getWidgets() {
        List<Widget__c> Widgets = [SELECT Name from Widget__c];
        return Widgets;
    }

    @HttpPost 
    global static String createNewWidget(String Name) {
        Widget__c w = new Widget__c();
        w.Name = Name;
        insert w;

        return 'Done';
   }
}