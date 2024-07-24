# Mitigating XSS with Security Headers

The code for a blog post I will publish that will show how SAST results will waste developer time on hygiene controls, whereas DAST will tell them if it's actually vulnerable.

I'll update it later with the actual blog post.

```bash
semgrep scan ./secure.py
```

<details open>
<summary>Semgrep results</summary>
<br>

```
┌─────────────────┐
│ 6 Code Findings │
└─────────────────┘
                            
    secure.py
   ❯❯❱ python.flask.security.dangerous-template-string.dangerous-template-string
          Found a template created with string formatting. This is susceptible to server-side template
          injection and cross-site scripting attacks.                                                 
          Details: https://sg.run/b79E                                                                
                                                                                                      
           27┆ template = '<h1>Hello, {}!</h1>'.format(name)
           28┆ return render_template_string(template)
   
    ❯❱ python.django.security.injection.raw-html-format.raw-html-format
          Detected user input flowing into a manually constructed HTML string. You may be accidentally       
          bypassing secure methods of rendering HTML by manually constructing HTML and this could create a   
          cross-site scripting vulnerability, which could let attackers steal sensitive user data. To be sure
          this is safe, check that the HTML is rendered safely. Otherwise, use templates                     
          (`django.shortcuts.render`) which will safely render HTML instead.                                 
          Details: https://sg.run/oYj1                                                                       
                                                                                                             
           27┆ template = '<h1>Hello, {}!</h1>'.format(name)
   
    ❯❱ python.flask.security.injection.raw-html-concat.raw-html-format
          Detected user input flowing into a manually constructed HTML string. You may be accidentally       
          bypassing secure methods of rendering HTML by manually constructing HTML and this could create a   
          cross-site scripting vulnerability, which could let attackers steal sensitive user data. To be sure
          this is safe, check that the HTML is rendered safely. Otherwise, use templates                     
          (`flask.render_template`) which will safely render HTML instead.                                   
          Details: https://sg.run/Pb7e                                                                       
                                                                                                             
           27┆ template = '<h1>Hello, {}!</h1>'.format(name)
   
    ❯❱ python.flask.security.audit.render-template-string.render-template-string
          Found a template created with string formatting. This is susceptible to server-side template
          injection and cross-site scripting attacks.                                                 
          Details: https://sg.run/8yjE                                                                
                                                                                                      
           28┆ return render_template_string(template)
   
     ❱ python.flask.debug.debug-flask.active-debug-code-flask
          The application is running debug code or has debug mode enabled. This may expose sensitive       
          information, like stack traces and environment variables, to attackers. It may also modify       
          application behavior, potentially enabling attackers to bypass restrictions. To remediate this   
          finding, ensure that the application's debug code and debug mode are disabled or removed from the
          production environment.                                                                          
          Details: https://sg.run/lBbpB                                                                    
                                                                                                           
           32┆ app.run(debug=True, port=5001)
   
    ❯❱ python.flask.security.audit.debug-enabled.debug-enabled
          Detected Flask app with debug=True. Do not deploy to production with this flag enabled as it will   
          leak sensitive information. Instead, consider using Flask configuration variables or setting 'debug'
          using system environment variables.                                                                 
          Details: https://sg.run/dKrd                                                                        
                                                                                                              
           32┆ app.run(debug=True, port=5001)

```

</details>