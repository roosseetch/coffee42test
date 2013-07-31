__author__ = 'Alfredo Saglimbeni'
import re
import uuid

from django.forms.widgets import  MultiWidget , to_current_timezone, DateInput
from datetime import datetime
from django.utils import translation

I18N  = """
$.fn.datetimepicker.dates['en'] = {
    days: %s,
    daysShort: %s,
    daysMin: %s,
    months: %s,
    monthsShort: %s,
    meridiem: %s,
    suffix: %s,
    today: %s
};
"""

datetimepicker_options = """
format : '%s',
startDate : '%s',
endDate : '%s',
weekStart : %s,
daysOfWeekDisabled : %s,
autoclose : %s,
startView : %s,
minView : %s,
maxView : %s,
todayBtn : %s,
todayHighlight : %s,
minuteStep : %s,
pickerPosition : '%s',
showMeridian : %s,
language : '%s',
"""

dateConversion = {
    'P' : '%p',
    'ss' : '%S',
    'ii' : '%M',
    'hh' : '%H',
    'HH' :  '%I',
    'dd' : '%d',
    'mm' : '%m',
    #'M' :  '%b',
    #'MM' : '%B',
    'yy' : '%y',
    'yyyy' : '%Y',
}
class DateWidget(MultiWidget):

    def __init__(self, attrs=None, options = {}):
        if attrs is None:
            attrs = {'readonly':''}

        self.option = ()
        self.option += (options.get('format','dd/mm/yyyy hh:ii'),)
        self.option += (options.get('startDate',''),)
        self.option += (options.get('endDate',''),)
        self.option += (options.get('weekStart','0'),)
        self.option += (options.get('daysOfWeekDisabled','[]'),)
        self.option += (options.get('autoclose','false'),)
        self.option += (options.get('startView','2'),)
        self.option += (options.get('minView','0'),)
        self.option += (options.get('maxView','4'),)
        self.option += (options.get('todayBtn','false'),)
        self.option += (options.get('todayHighlight','false'),)
        self.option += (options.get('minuteStep','5'),)
        self.option += (options.get('pickerPosition','bottom-right'),)
        self.option += (options.get('showMeridian','false'),)

        pattern = re.compile(r'\b(' + '|'.join(dateConversion.keys()) + r')\b')
        self.dataTimeFormat = self.option[0]
        self.format =  pattern.sub(lambda x: dateConversion[x.group()], self.option[0])

        widgets = (DateInput(attrs=attrs,format=self.format),)

        super(DateWidget, self).__init__(widgets, attrs)


    def value_from_datadict(self, data, files, name):
        date_time = [
                     widget.value_from_datadict(data, files, name + '_%s' % i)
                     for i, widget in enumerate(self.widgets)
                    ]
        try:
            D = to_current_timezone(datetime.strptime(date_time[0], self.format))
        except ValueError:
            return ''
        else:
            return D

    def decompress(self, value):
        if value:
            value = to_current_timezone(value)
            return (value,)
        return (None,)


    def format_output(self, rendered_widgets):
        """
        Given a list of rendered widgets (as strings), it inserts an HTML
        linebreak between them.

        Returns a Unicode string representing the HTML for the whole lot.
        """

        WEEKDAYS = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        WEEKDAYS_ABBR = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        WEEKDAYS_MIN = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
        MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        MONTHS_ABBR = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        MERIDIEN = ["am", "pm"]
        SUFFIX = ["st", "nd", "rd", "th"]
        TODAY = '"%s"' % ("Today")
        js_i18n = I18N % (WEEKDAYS,WEEKDAYS_ABBR, WEEKDAYS_MIN, MONTHS, MONTHS_ABBR, MERIDIEN, SUFFIX, TODAY)
        options = self.option+(translation.get_language(),)
        js_options = datetimepicker_options % options
        id = uuid.uuid4().hex
        return '<div id="%s"  class="input-append date form_datetime">'\
               '%s'\
               '<span class="add-on"><span class="glyphicon glyphicon-th"></span>'\
               '</div>'\
               '<script type="text/javascript">'\
               '%s$("#%s").datetimepicker({%s});'\
               '</script>  ' % ( id, rendered_widgets[0], js_i18n.replace(', u\'',', \'').replace('[u', '['), id , js_options)


    class Media:
        css = {
            'all' : ('css/datetimepicker.css',)
        }
        js = (
            "js/bootstrap-datetimepicker.js",
            )
