'use strict';

angular.module('djangularApp')
  .controller('MainCtrl', function ($scope, $http) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    $http({method: 'GET',url:'/api/person/?format=json'}).
        success(function(data,status,headers,config){
        	$scope.Persons = data.objects;
        });
  });
