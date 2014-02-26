'use strict';

angular.module('djangularApp')
  .controller('MainCtrl', function ($scope, $http) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    $http({method: 'GET',url:'/api/persons/'}).
        success(function(data,status,headers,config){
        	$scope.Persons = data;
          console.log(data);
        });
  });
