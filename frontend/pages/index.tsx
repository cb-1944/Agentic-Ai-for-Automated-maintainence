import { useRouter } from "next/router";

export default function Home() {
  const router = useRouter();

  return (
    <div className="relative min-h-screen overflow-hidden">

      {/* Background Image */}
      <div
        className="absolute inset-0 bg-cover bg-center brightness-75 backdrop-blur-sm scale-105"
        style={{
          backgroundImage: "url('/car.jpg')"// place image in /public
        }}
      />

      {/* Overlay (dulls image, preserves contrast) */}
      <div className="absolute inset-0 bg-white/80" />

      {/* Foreground Content */}
      <div className="relative z-10 min-h-screen flex flex-col items-center justify-center px-6 text-black">

        {/* Hero Title */}
        <h1 className="text-4xl md:text-5xl font-extrabold text-center max-w-3xl">
          Vehicle Health Intelligence
        </h1>

        {/* Subheading */}
        <p className="mt-4 text-lg text-gray-600 text-center max-w-2xl">
          Predictive maintenance, diagnostics, and service scheduling powered by AI.
        </p>

        {/* Role Selection */}
        <div className="mt-12 flex flex-col sm:flex-row gap-6">
          <button
            onClick={() => router.push("/customer/dashboard")}
            className="bg-black text-white px-8 py-3 text-lg font-semibold rounded-xl hover:bg-gray-900 transition"
          >
            I am a Customer
          </button>

          <button
            onClick={() => router.push("/service")}
            className="border border-black text-black px-8 py-3 text-lg font-semibold rounded-xl hover:bg-gray-100 transition"
          >
            I am a Service Center
          </button>
        </div>

        {/* Footer Line */}
        <p className="mt-10 text-sm text-gray-400 text-center max-w-xl">
          Choose your role to continue
        </p>

      </div>
    </div>
  );
}
