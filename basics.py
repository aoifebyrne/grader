{{extend 'layout.html'}}



<h1 color="DodgerBlue">Your classes:</h1>


<table class="table table-condensed table-bordered table-striped">
    <thead>
        <tr>
            <th> {{=T("Course ID")}} </th>
            <th> {{=T("Subject")}} </th>
        </tr>
    </thead>
    <tbody>
        {{for x in row:}}
        <tr> 
            <td>{{=x.course_id}} </td>
            <td>{{=x.subject}} </td>
        </tr>
{{pass}}
    </tbody>
</table>




<h2>
    Your students:
</h2>

<table class="table table-condensed table-bordered table-striped">
    <thead>
        <tr>
            <th> {{=T("Course ID")}} </th>
            <th> {{=T("Student ID")}} </th>
            <th> {{=T("Name")}} </th>
            <th> {{=T("Score")}} </th>
        </tr>
    </thead>
    <tbody>
        {{for x in gradetable:}}
        {{name=db((db.auth_user.id==x.student)).select(db.auth_user.first_name, db.auth_user.last_name)}}
        {{for y in name:}}
        <tr> 
            <td>{{=x.course_id}} </td>
            <td>{{=x.student}} </td>
            <td>{{=y.first_name}} {{=y.last_name}}</td>
            <td>{{=x.score}} </td>
        </tr>
{{pass}}
        {{pass}}
    </tbody>
</table>



<h2>
    Add or update student record:
</h2>

{{=form}}

<h2>Statistics</h2>
<table class="table table-condensed table-bordered table-striped">

    <tbody>
            <thead>
        <tr>
            
            <th></th>
            {{for x in row:}}
            <th> {{=x.course_id}} </th>
            {{pass}}
        </tr>
    </thead>
<tr>
    <td>Average:</td>
    <td>{{db(db.grades.course_id=='A2').score.max()}}</td>
            <td></td>    
        </tr>


    </tbody>
</table>



{{pass}}
