'use strict';

module.exports = function (grunt) {

  // Load grunt tasks automatically
  require('load-grunt-tasks')(grunt);

  // Time how long tasks take. Can help when optimizing build times
  require('time-grunt')(grunt);

  // Define the configuration for all the tasks
  grunt.initConfig({

    shell:{
      djangoServer:{
        options:{
          stdout:true
        },
        command: 'python manage.py runserver 127.0.0.1:8000'
      }
    },

    // Watches files for changes and runs tasks based on the changed files
    watch: {
      options: {
        livereload: true
      },
      html:{
        files:['templates/*.html','static/views/*.html']
      },
      css:{
        files:['static/styles/*.css']
      },
      js:{
        files:['static/scripts/*.js']
      },
      //insert tests here
      py:{
        files:['Djangular/*.py','backend/*.py']
      }
    }
  });
  
  grunt.loadNpmTasks('grunt-shell');

  grunt.registerTask('serve', function () {
    grunt.task.run([
      'shell:djangoServer',
      'watch'
    ]);
  });

  grunt.registerTask('server', function () {
    grunt.log.warn('The `server` task has been deprecated. Use `grunt serve` to start a server.');
    grunt.task.run(['serve']);
  });
};
