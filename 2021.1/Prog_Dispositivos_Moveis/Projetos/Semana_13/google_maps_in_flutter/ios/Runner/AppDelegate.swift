import UIKit
import Flutter
import GoogleMaps

@UIApplicationMain
@objc class AppDelegate: FlutterAppDelegate {
  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    GeneratedPluginRegistrant.register(with: self)

    //Add your API key
    GMSServices.provideAPIKey("AIzaSyAn-FdjT0rvJWetawwiFcvuR9i6ooNfnEE")
    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }
}
