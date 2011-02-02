from django.db import connections
from django.template import Template, Context
from django.conf import settings

#
# Log all SQL statements direct to the console (when running in DEBUG)
# Intended for use with the django development server.
#

class SQLLogToConsoleMiddleware(object):
    def process_response(self, request, response): 
      if settings.DEBUG:
        for connection_name in connections:
          connection = connections[connection_name]
          if connection.queries:
            time = sum([float(q['time']) for q in connection.queries])        
            header_t = Template("{{name}}: {{count}} quer{{count|pluralize:\"y,ies\"}} in {{time}} seconds")
            print header_t.render(Context({
              'name': connection_name, 
              'sqllog':connection.queries,
              'count':len(connection.queries),
              'time':time
            }))
            t = Template("{% for sql in sqllog %}[{{forloop.counter}}] {{sql.time}}s: {{sql.sql|safe}}{% if not forloop.last %}\n\n{% endif %}{% endfor %}")
            print t.render(Context({'sqllog':connection.queries}))                
      return response