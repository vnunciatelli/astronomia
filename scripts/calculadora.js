function calculate() {
    let aperture = parseFloat(document.getElementById("aperture").value);
    let focalRatio = parseFloat(document.getElementById("focalRatio").value);
    let eyepiece = parseFloat(document.getElementById("eyepiece").value);
    let apparentField = parseFloat(document.getElementById("apparentField").value);
    let barlow = parseFloat(document.getElementById("barlow").value) || 1;
    let focalReducer = parseFloat(document.getElementById("focalReducer").value) || 1;
    
    let focalLength = aperture * focalRatio * barlow / focalReducer;
    let magnification = focalLength / eyepiece;
    let trueFieldOfView = apparentField / magnification;
    let exitPupil = aperture / magnification;
    let resolvingPower = 116 / aperture;
    let limitingMagnitude = 2 + 5 * Math.log10(aperture);

    let output = `
        <p><strong>Comprimento Focal:</strong> ${focalLength.toFixed(2)} mm</p>
        <p><strong>Magnificação:</strong> ${magnification.toFixed(2)}x</p>
        <p><strong>Campo de Visão Real:</strong> ${trueFieldOfView.toFixed(2)}°</p>
        <p><strong>Pupila de Saída:</strong> ${exitPupil.toFixed(2)} mm</p>
        <p><strong>Poder Resolutivo Teórico:</strong> ${resolvingPower.toFixed(2)} segundos de arco</p>
        <p><strong>Magnitude Limite Aproximada:</strong> +${limitingMagnitude.toFixed(1)}</p>
    `;
    
    document.getElementById("output").innerHTML = output;
}