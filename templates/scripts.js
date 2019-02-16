// Holds all common scripts
var sessionID = -1;
// Runs on load
$(document).ready(function() {

});



// Hacky header script
function printHeaderMentor() {
    var header = "";
    header += "<div class=\"jumbotron professor\" id=\"jumbo\">";
    header += "<a href=\"home.html\"><img alt=\"logo\" src=\"../logotemp.png\" height=\"100\"></a>";
    header += "<a class=\"nav-link-prof\" href=\"mentorpage.html\" id=\"qSets\" " +
        "style=\"margin-left: 40px;\">FIND A MENTOR </a>";
    //header += "<a class=\"nav-link-prof\" href=\"qlist.html\" id=\"viewQs\">VIEW QUESTIONS</a>";
    //header += "<a class=\"nav-link-prof\" href=\"grades.html\" id=\"viewGrades\">VIEW GRADES</a>";
    //header += "<a class=\"nav-link-prof\" href=\"roster.html\" id=\"viewRoster\">VIEW ROSTER</a>";
    header += "</div>"
    document.write(header);
}


// Hacky header script
function printHeaderLanding() {
    var header = "";
    header += "<div class=\"jumbotron landing\" id=\"jumbo\">";
    header += "<a href=\"index.php\"><img alt=\"logo\" src=\"logo-2.0.png\" height=\"100\"></a>";
    header += "</div>";
    document.write(header);

}


