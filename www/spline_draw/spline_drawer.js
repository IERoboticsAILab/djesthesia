import * as THREE from "three";

// general setup, boring, skip to the next comment
var scene = new THREE.Scene();
    scene.background = new THREE.Color( 'black' );

var camera = new THREE.OrthographicCamera( -innerWidth/2, innerWidth/2, innerHeight/2, -innerHeight/2, -10, 10 );
    camera.position.set( 0, 0, 10 );
    camera.lookAt( scene.position );

var renderer = new THREE.WebGLRenderer( {antialias: true} );
    renderer.setSize( innerWidth, innerHeight );
    document.body.appendChild( renderer.domElement );
			
window.addEventListener( "resize", (event) => {
    camera.updateProjectionMatrix( );
    renderer.setSize( innerWidth, innerHeight );
		renderer.render( scene, camera );
});

// next comment
// create a spline curve and a line to visualize it
var curve = new THREE.SplineCurve( [] ),
		spline = new THREE.Line( 
				new THREE.BufferGeometry(),
				new THREE.LineBasicMaterial( { color: 'skyblue' } )
		);

scene.add( spline );
renderer.render( scene, camera);

var x_umh0, y_umh0, z_umh0;
var x_umh1, y_umh1, z_umh1;

var drawing;

while(true) {
	var promise0 = new Promise(function(resolve, reject) {
		var xhr = new XMLHttpRequest(),
			method = "GET",
			url = "http://127.0.0.1:8001/pose";
	
		xhr.open(method, url, true);
		xhr.onreadystatechange = function() {
			if (xhr.readyState === 4 && xhr.status === 200) {
			resolve(JSON.parse(xhr.responseText));
			}
		};
		xhr.send();
		});

	promise0.then(function(value) {
        x_umh0 = parseInt(value[0])
        y_umh0 = parseInt(value[1])
        z_umh0 = parseInt(value[2])
		// console.log("umh0 raw", x_umh0, y_umh0, z_umh0);

    });

	var promise1 = new Promise(function(resolve, reject) {
		var xhr = new XMLHttpRequest(),
			method = "GET",
			url = "http://127.0.0.1:8002/pose";
	
		xhr.open(method, url, true);
		xhr.onreadystatechange = function() {
			if (xhr.readyState === 4 && xhr.status === 200) {
			resolve(JSON.parse(xhr.responseText));
			}
		};
		xhr.send();
		});

	promise1.then(function(value) {
		x_umh1 = parseInt(value[0])
		y_umh1 = parseInt(value[1])
		z_umh1 = parseInt(value[2])
		// console.log("umh1 raw", x_umh1, y_umh1, z_umh1);
    });

	if(trigger_eq())
	{
		// console.log("window size", -innerWidth/2, innerWidth/2, innerHeight/2, -innerHeight/2);
		// click coordinates
		var x = parseInt(- x_umh0 + 1200), y = parseInt(- y_umh0 - 480);
		console.log("x and y", x, y)

		// draw a black circle to indicate dot position
		var point = new THREE.Mesh(
						new THREE.CircleGeometry(7),
						new THREE.MeshBasicMaterial( {color: 'yellow' })
				)
				point.position.set( x, y, 0 );
				scene.add( point );

		// add the point to the curve
		curve.points.push( new THREE.Vector2(x,y) );
		// console.log("curve len after", curve.points.length);
		curve = new THREE.SplineCurve( curve.points );
		var points = curve.getPoints( 20*curve.points.length );

		// regenerate its image
		spline.geometry.dispose( );
		spline.geometry = new THREE.BufferGeometry();
		spline.geometry.setFromPoints( points );

		drawing = true;
	}

	if(!trigger_eq() && drawing == true)
	{
		clear_scene();
		drawing = false;
	}
		
	renderer.render( scene, camera );
	await sleep(0.01)
}

function trigger_eq(){
	if (z_umh1 > 700 && z_umh1 < 900)
		if (x_umh1 > 850  && x_umh1 < 1050)
			if (y_umh1 > -450 && y_umh1 < -350)
				// console.log("The eq is triggered")
				return true;
	return false;
}

function clear_scene(){
	location.reload();
}

function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
  }


